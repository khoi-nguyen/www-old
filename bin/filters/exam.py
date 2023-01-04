#!/usr/bin/env python

import panflute as pf


def exam(element: pf.Element, doc: pf.Doc) -> None | pf.Element:
    """Create an exam class LaTeX document

    - Convert headers to questsion/parts
    - Convert divs to environments when applicable
    """

    if doc.format != "latex":
        return None

    if isinstance(element, pf.Header):
        cmd: list[str] = ["", "titledquestion", "part"]
        tex: str = "\\" + cmd[element.level]
        if element.level == 1:
            if pf.stringify(element):
                tex += "{" + pf.stringify(element) + "}"
            else:
                tex = tex.replace("titledquestion", "question")
        if "marks" in element.attributes:
            tex += f"[{element.attributes['marks']}]"
        question = pf.RawBlock(tex, format="latex")
        return question

    if isinstance(element, pf.Div) and len(element.classes) == 1:
        env: str = element.classes[0]
        begin, end = r"\begin{" + env + "}", r"\end{" + env + "}"
        element.content.insert(0, pf.RawBlock(begin, format="latex"))
        element.content.append(pf.RawBlock(end, format="latex"))
        return element


if __name__ == "__main__":
    pf.toJSONFilter(exam)
