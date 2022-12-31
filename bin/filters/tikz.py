#!/usr/bin/env python

import hashlib
import os
import pathlib
import subprocess

import panflute as pf

template = r"""
\documentclass{standalone}
\usepackage{amsmath,amssymb}
\usepackage{tikz}
\begin{document}
\usetikzlibrary{arrows}
\scalebox{%s}{
\begin{tikzpicture}
%s
\end{tikzpicture}
}
\end{document}
"""


def tikz(element, doc):
    if not isinstance(element, pf.CodeBlock) or not "tikz" in element.classes:
        return element
    scale = str(element.attributes.get("scale", 2))
    code = template % (scale, element.text)
    pathlib.Path("build/tikz").mkdir(parents=True, exist_ok=True)
    tmp = "build/tikz/" + hashlib.sha256(code.encode("utf-8")).hexdigest()
    if not os.path.exists(tmp + ".png"):
        with open(tmp + ".tex", "w+") as file:
            file.write(code)
        cmds = [
            ["latexmk", "-pdf", "-cd", "-f", tmp + ".tex"],
            [
                "convert",
                "-quality",
                "100",
                "-density",
                "150",
                "-flatten",
                "-trim",
                tmp + ".pdf",
                tmp + ".png",
            ],
        ]
        for cmd in cmds:
            subprocess.run(cmd, stdout=subprocess.DEVNULL)
    tmp = tmp.replace("build/", "/")
    output = pf.RawBlock(f"""<img src="{tmp}.png">""", format="html")
    return pf.Div(output, classes=["text-center"] + element.classes)


if __name__ == "__main__":
    pf.toJSONFilter(tikz)
