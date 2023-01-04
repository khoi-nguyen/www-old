#!/usr/bin/env python

import hashlib
import os
import pathlib
import subprocess

import panflute as pf


PATH: str = "build/figures/"
ROOT: str = "/figures/"
TEMPLATE: str = r"""
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


def tikz(element: pf.Element, doc: pf.Doc) -> None | pf.Element:
    """Replace CodeBlocks.tikz with a PNG image of the figure"""
    del doc
    if not isinstance(element, pf.CodeBlock) or "tikz" not in element.classes:
        return None

    # Get code
    scale: str = element.attributes.get("scale", "1")
    code: str = TEMPLATE % (scale, element.text)

    # Useful paths
    basename: str = hashlib.sha256(code.encode("utf-8")).hexdigest()
    tmp: str = PATH + basename
    src: str = ROOT + basename + ".png"

    # Generating the image if necessary
    pathlib.Path(PATH).mkdir(parents=True, exist_ok=True)
    if not os.path.exists(tmp + ".png"):
        with open(tmp + ".tex", "w+") as file:
            file.write(code)
        cmds: list[list[str]] = [
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

    # Creating the plot element
    img: pf.Element = pf.Para(pf.Image(url=src))
    return pf.Div(img, classes=["text-center"] + element.classes)


if __name__ == "__main__":
    pf.toJSONFilter(tikz)
