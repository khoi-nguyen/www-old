import json
import os
import typing

import flask
import flask_login
import flask_socketio
import werkzeug

DEBUG = os.environ.get("ENVIRONMENT", "") != "production"

app = flask.Flask(__name__, template_folder="templates")
app.secret_key = os.environ.get("SECRET_KEY", "hello").encode("UTF-8")
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


# ================
# Login and logout
# ================

login_manager = flask_login.LoginManager()
login_manager.init_app(app)


admin = flask_login.UserMixin()
setattr(admin, "id", "admin")


@login_manager.user_loader
def load_user(user_id: str) -> flask_login.UserMixin | None:
    if user_id == "admin":
        return admin
    return None


@app.route("/login", methods=["POST"])
def login() -> werkzeug.Response:
    data = flask.request.form
    if data.get("password") != os.environ.get("PASSWORD", "admin"):
        raise ValueError("Incorrect password")
    flask_login.login_user(admin, remember=True)
    return flask.redirect("/")


@app.route("/logout", methods=["GET"])
def logout() -> werkzeug.Response:
    flask_login.logout_user()
    redirect = flask.request.args.get("redirect")
    if redirect:
        return flask.redirect(redirect)
    return flask.jsonify({"success": True})


# ===========
# Whiteboards
# ===========

socketio = flask_socketio.SocketIO(app, logger=DEBUG)


class Stroke(typing.TypedDict):
    color: str
    lineWidth: int
    points: list[list[float]]


BoardList = list[list[list[Stroke]]]


@app.route("/socketio/<path:url>", methods=["POST"])
@flask_login.login_required
def socket(url: str = "") -> werkzeug.Response:
    json = flask.request.get_json() or {}
    json.update({"url": "/" + url})
    socketio.emit("changeReceived", json, broadcast=True)
    return flask.jsonify({"success": True})


@app.route("/boards/<path:url>", methods=["POST"])
@flask_login.login_required
def save_board(url: str = "") -> werkzeug.Response:
    boards: BoardList = flask.request.get_json() or []
    with open(url + ".json", "w") as file:
        file.write(json.dumps(clean(boards), separators=(",", ":")))
    return flask.jsonify({"success": True})


def clean(boards: BoardList) -> BoardList:
    """Delete empty strokes from a board list"""
    for slide in boards:
        for board in slide:
            for i, stroke in enumerate(board):
                if len(stroke["points"]) == 0:
                    del board[i]
    return boards


# =============
# Static routes
# =============


@app.route("/")
@app.route("/<path:url>")
def default_route(url: str = "") -> werkzeug.Response | str:
    if url == "favicon.ico":
        return flask.send_file("static/favicon.ico")

    # Protect metadata files and send board files instead
    if url.endswith(".json") and os.path.exists(url):
        return flask.send_file(url)

    # Adapt path
    url = "build/" + url
    if url.endswith("/") or not url:
        url += "index.html"
    elif "." not in url:
        url += ".html"

    # Serve file or trigger 404 error
    if not os.path.exists(url) or url.endswith(".json"):
        flask.abort(404)
    if url.endswith(".html"):
        return render_page(url)
    return flask.send_file(url)


def render_page(path: str) -> str:
    """Render a static HTML page"""

    def file_contents(path: str) -> str:
        with open(path) as f:
            return f.read()

    # Collect metadata
    json_path: str = path.replace(".html", ".json")
    data: dict[str, typing.Any] = json.loads(file_contents(json_path))
    data.update({"user": flask_login.current_user})

    # Render subtemplate
    content: str = flask.render_template_string(file_contents(path), **data)

    # Render master template if allowed
    data.update({"content": content})
    if data.get("private") and not getattr(data["user"], "is_authenticated"):
        return ""
    template_file: str = data.get("output", "") + ".html"
    return flask.render_template(template_file, **data)


# ==============
# Error handling
# ==============


@app.errorhandler(404)
def page_not_found(error):
    del error
    return render_page("build/404.html")


if __name__ == "__main__":
    socketio.run(app, debug=DEBUG)
