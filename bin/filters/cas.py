#!/usr/bin/env python

import ast
import importlib

import numpy as np
import panflute as pf
import sympy
import typing


class StackElement(typing.TypedDict):
    code: str
    stack: int


stack: list[StackElement] = []
CLASSES: set = {"sympy", "eval"}

_global = importlib.import_module("sympy").__dict__
_global.update({"np": np})
for letter in ["x", "y", "z", "t"]:
    _global[letter] = sympy.symbols(letter)
for letter in ["k", "m", "n"]:
    _global[letter] = sympy.symbols(letter, integer=True)


def exec_then_eval(code: str) -> str:
    global _global
    block = ast.parse(code, mode="exec")
    last = ast.Expression(getattr(block.body.pop(), "value"))
    exec(compile(block, "<string>", mode="exec"), _global, _global)
    return eval(compile(last, "<string>", mode="eval"), _global, _global)


def cas(element: pf.Element, doc: pf.Doc) -> None | pf.Element:
    del doc
    if not (
        isinstance(element, pf.Code) or isinstance(element, pf.CodeBlock)
    ) or not CLASSES & set(element.classes):
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
    result = exec_then_eval(code)
    if type(element) == pf.Code:
        return pf.Math(sympy.latex(result), format="InlineMath")
    return pf.Para(pf.Math(sympy.latex(result), format="DisplayMath"))


if __name__ == "__main__":
    pf.toJSONFilter(cas)
