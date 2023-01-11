#!/usr/bin/env python

import os
import subprocess
import tempfile
import textwrap
import typing

import panflute as pf
import sympy


class StackElement(typing.TypedDict):
    code: str
    stack: int


class Env(typing.TypedDict):
    code: str
    cmd: list[str]
    println: str


stack: list[StackElement] = []
LANG = typing.Literal["python", "julia"]
CONFIG: dict[LANG, Env] = {
    "python": {
        "code": textwrap.dedent(
            """
            import numpy as np
            from sympy import *
            x, y, z, t = symbols("x y z t")
            k, m, n = symbols("k m n", integer=True)
        """
        ),
        "cmd": ["env", "python"],
        "println": "print(%s)",
    },
    "julia": {
        "code": textwrap.dedent(
            """
            using SymPy
            @vars x y z t
            k, m, n = symbols("k m n", integer=True)
        """
        ),
        "cmd": ["env", "julia", "--project=."],
        "println": "println(%s)",
    },
}


def exec_then_eval(code: str, lang: LANG) -> str:
    name: str = ""
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp:
        name = tmp.name
        lines = code.split("\n")
        lines[-1] = CONFIG[lang]["println"] % lines[-1]
        tmp.write(CONFIG[lang]["code"] + "\n".join(lines))
    cmd = CONFIG[lang]["cmd"] + [name]
    out = subprocess.run(cmd, capture_output=True, text=True).stdout
    os.remove(name)
    try:
        expr = sympy.sympify(out)
        return sympy.latex(expr)
    except:
        return out


def cas(element: pf.Element, doc: pf.Doc) -> None | pf.Element:
    del doc
    if (
        not (isinstance(element, pf.Code) or isinstance(element, pf.CodeBlock))
        or "eval" not in element.classes
    ):
        return None

    # Reuse code from previous blocks if necessary
    code: str = ""
    for index, block in enumerate(stack):
        code += block["code"] + "\n"
        block["stack"] -= 1
        if not block["stack"]:
            del stack[index]

    # Save code for late use if necessary
    if element.attributes.get("stack"):
        stack.append({"code": element.text, "stack": int(element.attributes["stack"])})

    code += element.text
    lang = list(set(typing.get_args(LANG)) & set(element.classes))[0]
    result = exec_then_eval(code, lang or "python")
    if type(element) == pf.Code:
        return pf.Math(result, format="InlineMath")
    return pf.Para(pf.Math(result, format="DisplayMath"))


if __name__ == "__main__":
    pf.toJSONFilter(cas)
