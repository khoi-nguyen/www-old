#!/usr/bin/env python

import ast
import textwrap

import panflute as pf
import sympy

stack = []


def exec_then_eval(code):
    block = ast.parse(code, mode="exec")
    last = ast.Expression(block.body.pop().value)
    _globals, _locals = {}, {}
    exec(compile(block, "<string>", mode="exec"), _globals, _locals)
    return eval(compile(last, "<string>", mode="eval"), _globals, _locals)


def cas(element, doc):
    global stack
    if type(element) in [pf.Code, pf.CodeBlock] and "sympy" in element.classes:
        code = textwrap.dedent(
            """
            import numpy as np
            from sympy import *
            x, y, z, t = symbols("x y z t")
            k, m, n = symbols("k m n", integer=True)
        """
        )
        for index, block in enumerate(stack):
            code += block["code"] + "\n"
            block["stack"] -= 1
            if not block["stack"]:
                del stack[index]
        if element.attributes.get("stack"):
            stack.append(
                {"code": element.text, "stack": int(element.attributes.get("stack"))}
            )
        code += element.text
        result = exec_then_eval(code)
        if type(element) == pf.Code:
            return pf.Math(sympy.latex(result), format="InlineMath")
        return pf.Para(pf.Math(sympy.latex(result), format="DisplayMath"))


if __name__ == "__main__":
    pf.toJSONFilter(cas)
