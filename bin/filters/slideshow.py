#!/usr/bin/env python

import panflute as pf

first_slide: bool = True


def finalize(doc: pf.Doc):
    """Act on the document after the filter

    The aim of the filter is to wrap the slide contents inside a div.
    This can unfortunately only be done by closing and opening a new div
    every time we find a slide title.
    We need to close the last div.

    We also remove the first empty slide, used to define macros.
    """
    if doc.format == "revealjs":
        doc.content.pop(0)
        doc.content.append(pf.RawBlock("</div>", format="html"))


def prepare(doc: pf.Doc) -> None:
    """Act on the document before the filter

    - Automatically add the "row" class to slides that have columns inside them.
    - If 'split' is set to True, automatically split slides unless it has the 'nosplit' class.
    """
    if doc.format != "revealjs":
        return None

    has_columns = False
    default_split_value = getattr(doc, "get_metadata")("split", False)
    split = default_split_value
    for element in reversed(doc.content):
        if isinstance(element, pf.Header) and element.level == 1:
            if has_columns and "row" not in element.classes:
                element.classes.append("row")
            if (
                split
                and "split" not in element.classes
                and "nosplit" not in element.classes
            ):
                element.classes.append("split")
            has_columns = False
            split = default_split_value
        if isinstance(element, pf.Div) and "col" in element.classes:
            has_columns = True
            split = False


def slides(element: pf.Element, doc: pf.Doc) -> None | list[pf.Element]:
    """Wrap the slide contents in a div and customise the slide title

    - Try as much as possible to fit the slide contents inside a div
    - Add a clock to the slide title
    - Help to create columns in a less verbose syntax
    """
    if (
        doc.format != "revealjs"
        or not isinstance(element, pf.Header)
        or element.level > 1
    ):
        return None

    block_list: list[pf.Element] = []

    # Close the previous div if applicable
    global first_slide
    if first_slide:
        first_slide = False
    else:
        block_list.append(pf.RawBlock("</div>", format="html"))

    # Customize slide header
    element.classes.append("slide-title")
    clock = pf.RawInline("""<ticking-clock class="clock">""", format="html")
    element.content.append(clock)
    block_list.append(element)

    # Classes for slide contents container
    classes: list[str] = ["slide-contents"]
    if "row" in element.classes:
        element.classes.remove("row")
        classes.append("row")

    # Open a new div
    post = pf.RawBlock(f"""<div class="{' '.join(classes)}">""", format="html")
    block_list.append(post)

    return block_list


if __name__ == "__main__":
    pf.run_filter(slides, prepare=prepare, finalize=finalize)
