#!/usr/bin/env python

import hashlib
import pathlib
import os
import subprocess

import panflute as pf

template = r"""
\documentclass{standalone}
\usepackage{amsmath,amssymb}
\usepackage{tikz}
\begin{document}
\usetikzlibrary{arrows}
\scalebox{2}{
\begin{tikzpicture}
%s
\end{tikzpicture}
}
\end{document}
"""


def tikz(element, doc):
    if not isinstance(element, pf.CodeBlock) or not "tikz" in element.classes:
        return element
    code = template % element.text
    pathlib.Path("static/tikz").mkdir(parents=True, exist_ok=True)
    tmp = "static/tikz/" + hashlib.sha256(code.encode("utf-8")).hexdigest()
    if not os.path.exists(tmp + ".png"):
        with open(tmp + ".tex", "w+") as file:
            file.write(code)
        cmds = [
            ["latexmk", "-pdf", "-cd", "-f", tmp + ".tex"],
            ["convert", tmp + ".pdf", tmp + ".png"],
        ]
        for cmd in cmds:
            subprocess.run(cmd, stdout=subprocess.DEVNULL)
    output = pf.RawBlock(f"""<img src="/{tmp}.png">""", format="html")
    return pf.Div(output, classes=["text-center"] + element.classes)


if __name__ == "__main__":
    pf.toJSONFilter(tikz)
