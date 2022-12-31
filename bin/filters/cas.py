#!/usr/bin/env python

import ast
import importlib

import numpy as np
import panflute as pf
import sympy

stack = []

_global = importlib.import_module("sympy").__dict__
_global.update({"np": np})
for letter in ["x", "y", "z", "t"]:
    _global[letter] = sympy.symbols(letter)
for letter in ["k", "m", "n"]:
    _global[letter] = sympy.symbols(letter, integer=True)


def exec_then_eval(code):
    global _global
    block = ast.parse(code, mode="exec")
    last = ast.Expression(block.body.pop().value)
    exec(compile(block, "<string>", mode="exec"), _global, _global)
    return eval(compile(last, "<string>", mode="eval"), _global, _global)


def cas(element, doc):
    global stack
    if type(element) in [pf.Code, pf.CodeBlock] and "sympy" in element.classes:
        code = ""
        for index, block in enumerate(stack):
            code += block["code"] + "\n"
            block["stack"] -= 1
            if not block["stack"]:
                del stack[index]
        if element.attributes.get("stack"):
            stack.append(
                {"code": element.text, "stack": int(element.attributes["stack"])}
            )
        code += element.text
        result = exec_then_eval(code)
        if type(element) == pf.Code:
            return pf.Math(sympy.latex(result), format="InlineMath")
        return pf.Para(pf.Math(sympy.latex(result), format="DisplayMath"))


if __name__ == "__main__":
    pf.toJSONFilter(cas)
