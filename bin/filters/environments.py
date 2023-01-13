#!/usr/bin/env python

import panflute as pf

proofcount: int = 0


def environments(element: pf.Element, doc: pf.Doc):
    if not isinstance(element, pf.Div):
        return element
    envs: dict[str, dict] = getattr(doc, "get_metadata")("envs", {})
    if "solution" in element.classes:
        return collapsable_card(element, element.attributes.get("title", "Solution"))
    if "proof" in element.classes:
        return collapsable_card(element, "Proof")
    name = list(set(envs.keys()) & set(element.classes))
    if name:
        env = envs[name[0]]
        icon = ""
        if "icon" in env:
            icon = env["icon"]
        if "icon" in element.attributes:
            icon = element.attributes["icon"]
        icon = f"""<i class="{icon}"></i>""" if "icon" in env else ""
        header = f"""
        <h5 class="card-header {' '.join(env["classes"])}">
          {icon}
          <strong>{env.get("name", "")}</strong>
          {'(' if "title" in element.attributes and env.get("name") else ""}
          {element.attributes.get("title", "")}
          {')' if "title" in element.attributes and env.get("name") else ""}
        </h5>
      """
        header = pf.RawBlock(header, format="html")
        element.classes.append("card-body")
        container_classes = ["card"]
        if "fragment" in element.classes:
            element.classes.remove("fragment")
            container_classes.append("fragment")
        return pf.Div(header, element, classes=container_classes)


def collapsable_card(element, title="Solution"):
    global proofcount
    header = f"""
    <h5 data-bs-toggle="collapse" href="#proof{proofcount}" class="card-header">
      <strong>{title}</strong>
    </h5>
    """
    header = pf.RawBlock(header, format="html")
    element.classes += ["collapse", "card-body"]
    if not int(element.attributes.get("collapse", 1)):
        element.classes.remove("collapse")
    element.identifier = f"proof{proofcount}"
    proofcount += 1
    container_classes = ["card"]
    if "fragment" in element.classes:
        element.classes.remove("fragment")
        container_classes.append("fragment")
    return pf.Div(header, element, classes=container_classes)


if __name__ == "__main__":
    pf.toJSONFilter(environments)
