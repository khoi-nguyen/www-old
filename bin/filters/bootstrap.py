#!/usr/bin/env python

import panflute as pf


def bootstrapify(element: pf.Element, doc: pf.Doc) -> pf.Element | None:
    if type(element) == pf.Table and doc.format in ["html", "revealjs"]:
        element.classes.append("table")
        element.classes.append("table-striped")
        return element


if __name__ == "__main__":
    pf.toJSONFilter(bootstrapify)
