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
parser.add_argument("-o", "--output-file", type=str, required=False)
parser.add_argument("--meta-only", action="store_true")
parser.add_argument("--meta-file", type=str, default="")
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
cmd += ["--reference-location=block"]
if args.meta_only:
    cmd.append("--template=templates/json.html")
else:
    # Determining output format
    output: str = "html"
    if args.meta_file:
        with open(args.meta_file) as file:
            metadata = json.loads(file.read())
        output = metadata.get("output", "html")
    if output == "exam":
        cmd += ["-t", "latex", "--template=templates/exam.tex"]
    else:
        cmd += ["-t", output]

    # Add additional options
    cmd += ["--citeproc", "--csl", "templates/apa.csl"]
    cmd += ["--katex", "--email-obfuscation=javascript"]
    for pandocfilter in glob.glob("bin/filters/*.py"):
        cmd += ["--filter", pandocfilter]

output: str = subprocess.run(cmd, capture_output=True, text=True).stdout
if args.output_file:
    pathlib.Path(args.output_file).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output_file, "w") as file:
        file.write(output)
else:
    print(output)
