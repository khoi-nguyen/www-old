#!/usr/bin/env python

import panflute as pf

first_slide = True


def finalize(doc):
    if doc.format == "revealjs":
        doc.content.pop(0)
        doc.content.append(pf.RawBlock("</div>", format="html"))


def slides(element, doc):
    if doc.format == "revealjs" and type(element) == pf.Header:
        if element.level > int(doc.get_metadata("slide-level", default=1)):
            return element
        global first_slide
        pre = pf.RawBlock("</div>", format="html")
        classes = "slide-contents"
        if "row" in element.classes:
            element.classes.remove("row")
            classes += " row"
        post = pf.RawBlock(f"""<div class="{classes}">""", format="html")
        element.classes += ["slide-title", "position-relative"]
        cls = 'class="position-absolute top-50 end-0 translate-middle-y clock"'
        clock = pf.RawInline(f"<ticking-clock {cls}>", format="html")
        element.content.append(clock)
        if first_slide:
            first_slide = False
            return [element, post]
        return [pre, element, post]


if __name__ == "__main__":
    pf.run_filter(slides, finalize=finalize)
