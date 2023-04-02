#!/usr/bin/env python

import panflute as pf


def finalize(doc: pf.Doc) -> None:
    if doc.format != "latex":
        return None

    tex = pf.RawBlock(r"\end{parts}", format="latex")
    doc.content.append(tex)


def exam(element: pf.Element, doc: pf.Doc) -> None | pf.Element:
    """Create an exam class LaTeX document

    - Convert headers to questsion/parts
    - Convert divs to environments when applicable
    """

    if doc.format != "latex":
        return None

    if isinstance(element, pf.Header) and element.level == 1:
        tex = r"\question"
        if pf.stringify(element):
            tex = r"\titledquestion{" + pf.stringify(element) + "}"
        if "marks" in element.attributes:
            tex += f"[{element.attributes['marks']}]"
        tex += r"\begin{parts}"
        return pf.RawBlock(tex, format="latex")

    if isinstance(element, pf.Header) and element.level == 2:
        tex = r"\part"
        return pf.RawBlock(tex, format="latex")

    if isinstance(element, pf.Div) and len(element.classes) == 1:
        env: str = element.classes[0]
        begin, end = r"\begin{" + env + "}", r"\end{" + env + "}"
        element.content.insert(0, pf.RawBlock(begin, format="latex"))
        element.content.append(pf.RawBlock(end, format="latex"))
        return element


if __name__ == "__main__":
    pf.run_filter(exam, finalize=finalize)
