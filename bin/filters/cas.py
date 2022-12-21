#!/usr/bin/env python

import ast
import textwrap

import panflute as pf
import sympy


def exec_then_eval(code):
    block = ast.parse(code, mode="exec")
    last = ast.Expression(block.body.pop().value)
    _globals, _locals = {}, {}
    exec(compile(block, "<string>", mode="exec"), _globals, _locals)
    return eval(compile(last, "<string>", mode="eval"), _globals, _locals)


def cas(element, doc):
    if type(element) in [pf.Code, pf.CodeBlock] and "sympy" in element.classes:
        code = textwrap.dedent(
            f"""
            import numpy as np
            from sympy import *
            x, y, z, t = symbols("x y z t")
            k, m, n = symbols("k m n", integer=True)
        """
        )
        code += element.text
        result = exec_then_eval(code)
        if type(element) == pf.Code:
            return pf.Math(sympy.latex(result), format="InlineMath")
        return pf.Para(pf.Math(sympy.latex(result), format="DisplayMath"))


if __name__ == "__main__":
    pf.toJSONFilter(cas)
