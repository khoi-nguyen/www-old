#!/usr/bin/env python

import panflute as pf


def exam(element, doc):
    if isinstance(element, pf.Header):
        cmd = ["", "titledquestion", "part"]
        tex = "\\" + cmd[element.level]
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
        env = element.classes[0]
        begin, end = r"\begin{" + env + "}", r"\end{" + env + "}"
        element.content.insert(0, pf.RawBlock(begin, format="latex"))
        element.content.append(pf.RawBlock(end, format="latex"))
        return element


if __name__ == "__main__":
    pf.toJSONFilter(exam)
