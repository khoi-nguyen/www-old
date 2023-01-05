#!/usr/bin/env python

import argparse
import glob
import json
import os
import pathlib
import subprocess

# Parsing args
parser = argparse.ArgumentParser()
parser.add_argument("path", type=str)
parser.add_argument("--meta", default=False, type=bool)
args: argparse.Namespace = parser.parse_args()

# Getting source files
path: pathlib.Path = pathlib.Path(args.path)
sources: list[str] = []
while path != pathlib.Path("."):
    if os.path.exists(path) and os.path.isfile(path):
        sources.append(str(path))
    path = path.parent
    meta_path: pathlib.Path = pathlib.Path(str(path) + "/meta.yaml")
    if os.path.exists(meta_path):
        sources.append(str(meta_path))
sources.reverse()

# Calling pandoc
cmd: list[str] = ["pandoc", "--quiet"] + sources
if args.meta:
    cmd.append("--template=templates/json.html")
else:
    # Determining output format
    with open("build/" + args.path.replace(".md", ".json"), "r") as file:
        metadata = json.loads(file.read())
    output: str = metadata.get("output", "html")
    if output == "exam":
        cmd += ["-t", "latex", "--template=templates/exam.tex"]
    else:
        cmd += ["-t", output]

    # Add additional options
    cmd += ["--citeproc", "--csl", "templates/apa.csl"]
    cmd += ["--mathjax", "--email-obfuscation=javascript"]
    for pandocfilter in glob.glob("bin/filters/*.py"):
        cmd += ["--filter", pandocfilter]
print(subprocess.run(cmd, capture_output=True, text=True).stdout)
