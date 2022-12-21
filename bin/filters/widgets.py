#!/usr/bin/env python

import glob
import json
import subprocess
import sys
import yaml

import jinja2
import panflute as pf


this_module = sys.modules[__name__]
environment = jinja2.Environment()


def widget(element, doc):
    if isinstance(element, pf.CodeBlock) and "widget" in element.classes:
        name = element.attributes.get("name")
        function = getattr(this_module, name)
        html = function(**yaml.safe_load(element.text))
        return pf.RawBlock(html, format="html")


def template(func):
    def wrapped(*args, **kwargs):
        wrapped.vars = kwargs
        template = func(wrapped, *args, **kwargs)
        template = environment.from_string(template)
        return template.render(**wrapped.vars)

    return wrapped


@template
def explorer(
    self,
    directory: str = ".",
    globstr: str = "*.md",
    order_by: str = "path",
    filters: dict = {},
):
    self.vars["files"] = []

    def last_modified(path):
        cmd = ["git", "log", "-1", "--pretty=%cd", "--date=format:%d %B %Y", path]
        return subprocess.check_output(cmd).decode("utf-8")

    for path in glob.glob(directory + "/" + globstr):
        json_path = "build/" + path.replace(".md", ".json")
        with open(json_path) as file:
            meta = json.loads(file.read())
        show = all([meta[key] == val for key, val in filters.items()])
        if show and not meta.get("private"):
            meta.update({
                "href": "/" + path.replace("index", "").replace(".md", ""),
                "last_modified": last_modified(path),
                "path": path,
            })
            self.vars["files"].append(meta)
    self.vars["files"].sort(key=lambda f: f[order_by])
    return """
      <ul>
        {% for file in files %}
        <li>
          <h5><a href="{{ file.href }}">{{ file.title }}</a></h5>
          {% if file.notes %}
          <p>{{ file.notes }}</p>
          {% endif %}
          <p><small>Last modified: {{ file.last_modified }}</small></p>
        </li>
        {% endfor %}
      </ul>
    """


def iframe(url: str, width: int | str = "100%", height: int | str = 900):
    return f"""
      <iframe src="{url}" width="{width}" height={height}">
      </iframe>
    """


def geogebra(url: str, width: int = 800, height: int = 600):
    url = url.split("/")[-1]
    url = f"https://www.geogebra.org/material/iframe/id/{url}"
    url += f"/width/{width}/height/{height}/ai/false/smb/false/stb/false"
    return f"""
      <iframe scrolling="no"
        src="{url}"
        height="{height}"
        width="{width}"
        style="border: 0px; margin: auto" allowfullscreen>
      </iframe>
    """


def pdf(url: str, width: int | str = "100%", height: int | str = 900):
    return f"""
      <object data="{url}" type="application/pdf"
        width="{width}"
        height={height}">
        <embed src="{url}" type="application/pdf">
        </embed>
      </object>
    """


if __name__ == "__main__":
    pf.toJSONFilter(widget)
