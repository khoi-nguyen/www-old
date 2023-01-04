#!/usr/bin/env python

import panflute as pf


def bootstrapify(element: pf.Element, doc: pf.Doc):
    if type(element) == pf.Table and doc.format == "html":
        element.classes.append("table")
        element.classes.append("table-striped")
        return element


if __name__ == "__main__":
    pf.toJSONFilter(bootstrapify)
