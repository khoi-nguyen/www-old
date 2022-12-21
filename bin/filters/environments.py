#!/usr/bin/env python

import panflute as pf

proofcount = 0

envs = {
    "algorithm": {
        "name": "Algorithm",
        "classes": ["bg-success", "text-dark", "text-white"],
        "icon": "fa-solid fa-code",
    },
    "alertblock": {
        "name": "",
        "classes": ["bg-danger", "text-dark", "text-white"],
    },
    "block": {
        "name": "",
        "classes": ["bg-primary", "text-dark", "text-white"],
    },
    "exampleblock": {
        "name": "",
        "classes": ["bg-success", "text-dark", "text-white"],
    },
    "definition": {
        "name": "Definition",
        "classes": ["bg-success", "text-dark", "text-white"],
        "icon": "fa-solid fa-book",
    },
    "example": {
        "name": "Example",
        "classes": ["bg-success", "text-dark", "text-white"],
        "icon": "fa-solid fa-pen-to-square",
    },
    "exercise": {
        "name": "Exercise",
        "classes": ["bg-success", "text-dark", "text-white"],
        "icon": "fa-solid fa-pencil",
    },
    "proposition": {
        "name": "Proposition",
        "classes": ["bg-primary", "text-dark", "text-white"],
        "icon": "fa-solid fa-book",
    },
    "question": {
        "name": "Question",
        "classes": ["bg-primary", "text-dark", "text-white"],
        "icon": "fa-solid fa-circle-question",
    },
    "remark": {
        "name": "Remark",
        "classes": ["bg-danger", "text-dark", "text-white"],
    },
    "task": {
        "name": "Task",
        "classes": ["bg-success", "text-dark", "text-white"],
        "icon": "fa-solid fa-laptop",
    },
    "theorem": {
        "name": "Theorem",
        "classes": ["bg-primary", "text-dark", "text-white"],
        "icon": "fa-solid fa-book",
    },
}


def environments(element, doc):
    if type(element) == pf.Div and "solution" in element.classes:
        return collapsable_card(element, "Solution")
    if type(element) == pf.Div and "proof" in element.classes:
        return collapsable_card(element, "Proof")
    elif type(element) == pf.Div:
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
              <strong>{env["name"]}</strong>
              {'(' if "title" in element.attributes and env["name"] else ""}
              {element.attributes.get("title", "")}
              {')' if "title" in element.attributes and env["name"] else ""}
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
    element.identifier = f"proof{proofcount}"
    proofcount += 1
    return pf.Div(header, element, classes=["card"])


if __name__ == "__main__":
    pf.toJSONFilter(environments)
