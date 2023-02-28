#!/usr/bin/env python

import panflute as pf


def jupyter(element: pf.Element, doc: pf.Doc) -> None | pf.Element:
    del doc
    if not isinstance(element, pf.CodeBlock) or "jupyter" not in element.classes:
        return None
    code: str = element.text
    lang: str = "julia"
    raw: str = f"""<pre data-executable="true" data-language="{lang}">{code}</pre>"""
    return pf.RawBlock(raw, format="html")


if __name__ == "__main__":
    pf.toJSONFilter(jupyter)
