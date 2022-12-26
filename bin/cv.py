#!/usr/bin/env python

import os
import subprocess
import sys

import jinja2
import yaml

output = sys.argv[-1]
lang = output[output.rfind("_") + 1 : -4]


def translate(data, lang="en"):
    if isinstance(data, list):
        return [translate(x, lang) for x in data]
    if isinstance(data, dict):
        translated = {
            key.replace("_" + lang, ""): val
            for key, val in data.items()
            if key.endswith("_" + lang)
        }
        data.update(translated)
        return {key: translate(val, lang) for key, val in data.items()}
    return data


with open("cv.yaml") as file:
    data = translate(yaml.safe_load(file.read()), lang)


def pandoc(text: str) -> str:
    process = subprocess.run(
        ["pandoc", "-t", "latex"], stdout=subprocess.PIPE, input=text, encoding="utf-8"
    )
    return process.stdout


env = jinja2.Environment(
    block_start_string=r"\block{",
    block_end_string="}",
    variable_start_string=r"\var{",
    variable_end_string="}",
    trim_blocks=True,
    autoescape=False,
    loader=jinja2.FileSystemLoader(os.path.abspath(".")),
)
env.filters["pandoc"] = pandoc

template = env.get_template("templates/cv.tex")
print(template.render(**data))
