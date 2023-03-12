#!/usr/bin/env python

import jinja2
import panflute as pf

proofcount: int = 0
environment = jinja2.Environment()


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
        env.update(element.attributes)
        header = environment.from_string(
            """
        <h5 class="card-header {{' '.join(env['classes'])}}">
          {% if env['icon'] %}
            <i class="{{env['icon']}}"></i>
          {% endif %}
          {% if env['name'] %}
            <strong>{{env['name']}}</strong>
            {% if env['title'] %}
            ({{env['title']}})
            {% endif %}
          {% else %}
            <strong>{{env['title']}}</strong>
          {% endif %}
        </h5>
      """
        ).render(env=env)
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
