#!/usr/bin/env python

import hashlib
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
) -> str:
    self.vars["files"] = []

    def last_modified(path):
        cmd = ["git", "log", "-1", "--pretty=%cd", "--date=format:%d %b %Y %H:%m", path]
        return subprocess.check_output(cmd).decode("utf-8")

    for path in glob.glob(directory + "/" + globstr):
        json_path = "build/" + path.replace(".md", ".json")
        with open(json_path) as file:
            meta = json.loads(file.read())
        show = all([meta[key] == val for key, val in filters.items()])
        if show and not meta.get("private"):
            meta.update(
                {
                    "href": "/" + path.replace("index", "").replace(".md", ""),
                    "last_modified": last_modified(path),
                    "path": path,
                    "source": f"https://github.com/khoi-nguyen/www/blob/master/{path}?plain=1",
                }
            )
            self.vars["files"].append(meta)
    self.vars["files"].sort(key=lambda f: f[order_by])
    return """
      <div class="list-group container">
        {% for file in files %}
        <div class="list-group-item list-group-item-action">
          <div class="d-flex w-100 justify-content-between">
            <h5 class="mb-1">{{ file.title }}</h5>
            <small class="text-muted">Last modified: {{ file.last_modified }}</small>
          </div>
          <ul class="text-muted list-inline small">
            <li class="list-inline-item small"><a href="{{ file.href }}"><i class="fa-brands fa-slideshare"></i> Slides</a></li>
            <li class="list-inline-item small"><a href="{{ file.href }}?fragments=false"><i class="fa-solid fa-display"></i> Without transitions</a></li>
            <li class="list-inline-item small"><a href="{{ file.source }}"><i class="fa-solid fa-code"></i> Source</a></li>
          </ul>
          {% if file.notes %}
          <p class="small">{{ file.notes }}</p>
          {% endif %}
        </div>
        {% endfor %}
      </div>
    """


def iframe(url: str, width: int | str = "100%", height: int | str = 900) -> str:
    return f"""
      <iframe src="{url}" width="{width}" height={height}">
      </iframe>
    """


def geogebra(url: str, width: int = 800, height: int = 600) -> str:
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
    
def a4(url: str):
    url += "#view=FitH&toolbar=0"
    ident = hashlib.sha256(url.encode("utf-8")).hexdigest()
    return f"""
      <object data="{url}" type="application/pdf" width="100%" id="{ident}">
        <embed src="{url}" type="application/pdf" id="{ident}">
        </embed>
      </object>
      <script type="text/javascript">
        const pdf = document.getElementById("{ident}");
        const resizeObserver = new ResizeObserver(function () {{
          pdf.setAttribute("height", 1.414 * pdf.offsetWidth);
        }});
        resizeObserver.observe(pdf)
      </script>
    """


def pdf(url: str, width: int | str = "100%", height: int | str = 900) -> str:
    return f"""
      <object data="{url}" type="application/pdf"
        width="{width}" height="{height}">
        <embed src="{url}" type="application/pdf">
        </embed>
      </object>
    """


if __name__ == "__main__":
    pf.toJSONFilter(widget)
