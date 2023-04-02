#!/usr/bin/env python

import panflute as pf


first_part = True
close_parts = False


def finalize(doc: pf.Doc) -> None:
    if doc.format != "latex":
        return None

    doc.content.pop(0)

    global close_parts
    if close_parts:
        tex = pf.RawBlock(r"\end{parts}", format="latex")
        doc.content.append(tex)


def exam(element: pf.Element, doc: pf.Doc) -> None | pf.Element:
    """Create an exam class LaTeX document

    - Convert headers to questsion/parts
    - Convert divs to environments when applicable
    """

    if doc.format != "latex":
        return None

    global first_part, close_parts

    if isinstance(element, pf.Header) and element.level == 1:
        tex = ""
        if close_parts:
            tex = r"\end{parts}" + "\n\n"
            close_parts = False
            first_part = True
        if pf.stringify(element):
            tex += r"\titledquestion{" + pf.stringify(element) + "}"
        else:
            tex += r"\question"
        if "marks" in element.attributes:
            tex += f"[{element.attributes['marks']}]"
        return pf.RawBlock(tex, format="latex")

    if isinstance(element, pf.Header) and element.level == 2:
        tex = ""
        if first_part:
            tex += r"\begin{parts}"
            first_part = False
            close_parts = True
        tex += r"\part"
        if "marks" in element.attributes:
            tex += f"[{element.attributes['marks']}]"
        return pf.RawBlock(tex, format="latex")

    if isinstance(element, pf.Div) and len(element.classes) == 1:
        env: str = element.classes[0]
        begin, end = r"\begin{" + env + "}", r"\end{" + env + "}"
        element.content.insert(0, pf.RawBlock(begin, format="latex"))
        element.content.append(pf.RawBlock(end, format="latex"))
        return element


if __name__ == "__main__":
    pf.run_filter(exam, finalize=finalize)
