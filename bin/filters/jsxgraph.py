#!/usr/bin/env python

import hashlib

import panflute as pf

TEMPLATE: str = """
<script type="text/javascript">
const board = new JSXBoard("%s");
%s
</script>
"""


def jsxgraph(element: pf.Element, doc: pf.Doc) -> list[pf.Element] | None:
    del doc
    if not isinstance(element, pf.CodeBlock) or "jsxgraph" not in element.classes:
        return None

    div = pf.Div()
    alt_id: str = hashlib.sha256(element.text.encode("utf-8")).hexdigest()
    div.identifier = element.identifier or alt_id
    div.classes += ["jxgbox"]
    width: str = element.attributes.get("width", "500")
    height: str = element.attributes.get("height", "500")
    div.attributes = {"style": f"width: {width}px; height: {height}px; margin: auto;"}
    div.attributes.update(element.attributes)
    js = pf.RawBlock(TEMPLATE % (div.identifier, element.text), format="html")
    return [div, js]


if __name__ == "__main__":
    pf.toJSONFilter(jsxgraph)
