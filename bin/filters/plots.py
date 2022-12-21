#!/usr/bin/env python

import hashlib
import os
import pathlib
import subprocess

import panflute as pf

config = {
    "python": {
        "code": """
import matplotlib
from matplotlib.pyplot import *
rcParams["text.usetex"] = True
matplotlib.use("Agg")
from numpy import *
%s
savefig("%s.svg")
        """,
        "cmd": ["env", "python"],
    },
    "julia": {
        "code": """
ENV["GKSwstype"] = "nul"
using Plots
using LaTeXStrings
default(linewidth=2)
%s
savefig("%s.svg")
        """,
        "cmd": ["env", "julia", "--project=."],
    },
}


def plot(element, doc):
    if isinstance(element, pf.CodeBlock) and "plot" in element.classes:
        lib = set(config.keys()) & set(element.classes)
        if not lib:
            return element
        lib = config[list(lib)[0]]
        to_hash = lib["code"] + element.text
        pathlib.Path("static/plots").mkdir(parents=True, exist_ok=True)
        tmp = "static/plots/" + hashlib.sha256(to_hash.encode("utf-8")).hexdigest()
        if not os.path.exists(tmp + ".svg"):
            with open(tmp, "w+") as file:
                file.write(lib["code"] % (element.text, tmp))
            subprocess.run(lib["cmd"] + [tmp], stdout=subprocess.DEVNULL)
        output = pf.RawBlock(f"""<img src="/{tmp}.svg">""", format="html")
        return pf.Div(output, classes=["text-center"])


if __name__ == "__main__":
    pf.toJSONFilter(plot)
