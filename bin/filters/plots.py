#!/usr/bin/env python

import hashlib
import os
import pathlib
import subprocess
import textwrap
import typing

import panflute as pf


class PlotEnv(typing.TypedDict):
    code: str
    cmd: list[str]
    ext: str


CONFIG: dict[str, PlotEnv] = {
    "python": {
        "code": textwrap.dedent(
            """
            import matplotlib
            from matplotlib.pyplot import *
            rcParams["text.usetex"] = True
            matplotlib.use("Agg")
            from numpy import *
            %s
            savefig("%s.svg")
        """
        ),
        "ext": ".py",
        "cmd": ["env", "python"],
    },
    "julia": {
        "code": textwrap.dedent(
            """
            ENV["GKSwstype"] = "nul"
            using Plots
            using LaTeXStrings
            default(linewidth=2)
            %s
            savefig("%s.svg")
        """
        ),
        "ext": ".jl",
        "cmd": ["env", "julia", "--project=."],
    },
}
PATH = "build/figures/"
ROOT = "/figures/"


def plot(element: pf.Element, doc: pf.Doc) -> None | pf.Element:
    """Replaces code blocks by a plot when appropriate

    At the moment, only matlplotlib (Python) and Plots (Julia) are supported.
    """
    del doc
    if not isinstance(element, pf.CodeBlock) or "plot" not in element.classes:
        return None

    # Determine the plotting environment (e.g. matplotlib)
    candidates = list(set(CONFIG.keys()) & set(element.classes))
    if not candidates:
        return None
    env: PlotEnv = CONFIG[candidates[0]]

    # Determine the plot's filename
    to_hash: bytes = (env["code"] + element.text).encode("utf-8")
    basename: str = hashlib.sha256(to_hash).hexdigest()
    tmp: str = PATH + basename
    src: str = ROOT + basename + ".svg"

    # Generating the plot if necessary
    pathlib.Path(PATH).mkdir(parents=True, exist_ok=True)
    if not os.path.exists(tmp + ".svg"):
        with open(tmp + env["ext"], "w+") as file:
            file.write(env["code"] % (element.text, tmp))
        subprocess.run(env["cmd"] + [tmp + env["ext"]], stdout=subprocess.DEVNULL)

    img = pf.Para(pf.Image(url=src))
    return pf.Div(img, classes=["text-center"] + element.classes)


if __name__ == "__main__":
    pf.toJSONFilter(plot)
