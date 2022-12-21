#!/usr/bin/env python

import base64
import hashlib
import os
import pathlib
import subprocess

import panflute as pf


def mermaid(element, doc):
    if type(element) == pf.CodeBlock and "mermaid" in element.classes:
        pathlib.Path("tmp").mkdir(parents=True, exist_ok=True)
        tmp = "tmp/" + hashlib.sha256(element.text.encode("utf-8")).hexdigest()
        if not os.path.exists(tmp + ".png"):
            with open(tmp, "w+") as file:
                file.write(element.text)
            subprocess.call(["mmdc", "-i", tmp, "-o", tmp + ".png", "-q"])
        with open(tmp + ".png", "rb") as file:
            image = base64.b64encode(file.read()).decode()
        html = f"""<img src="data:image/png;base64,{image}"/>"""
        output = pf.RawBlock(html, format="html")
        return pf.Div(output, classes=["text-center"])


if __name__ == "__main__":
    pf.toJSONFilter(mermaid)
