#!/usr/bin/env python

import panflute as pf


def bootstrapify(element, doc):
    if type(element) == pf.Table:
        element.classes.append("table")
        element.classes.append("table-striped")
        return element


if __name__ == "__main__":
    pf.toJSONFilter(bootstrapify)
