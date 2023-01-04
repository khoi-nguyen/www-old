import json
import os

import flask
import flask_login
import flask_socketio

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
def load_user(user_id):
    if user_id == "admin":
        return admin
    return None


@app.route("/login", methods=["POST"])
def login():
    data = flask.request.form
    if data.get("password") != os.environ.get("PASSWORD", "admin"):
        raise ValueError(data)
    flask_login.login_user(admin, remember=True)
    return flask.redirect("/")


@app.route("/logout", methods=["GET"])
def logout():
    flask_login.logout_user()
    redirect = flask.request.args.get("redirect")
    if redirect:
        return flask.redirect(redirect)
    return flask.jsonify({"success": True})


# ===========
# Whiteboards
# ===========

socketio = flask_socketio.SocketIO(app, logger=DEBUG)


@app.route("/socketio/<path:url>", methods=["POST"])
@flask_login.login_required
def socket(url: str = ""):
    json = flask.request.get_json() or {}
    json.update({"url": "/" + url})
    socketio.emit("changeReceived", json, broadcast=True)
    return flask.jsonify({"success": True})


@app.route("/boards/<path:url>", methods=["POST"])
@flask_login.login_required
def save_board(url: str = ""):
    boards = flask.request.get_json() or []
    with open(url + ".json", "w") as file:
        file.write(json.dumps(clean(boards), separators=(",", ":")))
    return flask.jsonify({"success": True, "boards": boards})


def clean(boards):
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
def default_route(url: str = ""):
    if url == "favicon.ico":
        return flask.send_file("static/favicon.ico")

    if url.endswith("/") or not url:
        url += "index.html"
    elif "." not in url:
        url += ".html"

    # Protect metadata files and send board files instead
    if url.endswith(".json") and os.path.exists(url):
        return flask.send_file(url)

    url = "build/" + url
    if not os.path.exists(url) or url.endswith(".json"):
        flask.abort(404)
    if url.endswith(".html"):
        return render_page(url)
    return flask.send_file(url)


def render_page(path: str) -> str:
    def file_contents(path: str) -> str:
        with open(path) as f:
            return f.read()

    data = json.loads(file_contents(path.replace(".html", ".json")))
    data["user"] = flask_login.current_user
    content = flask.render_template_string(file_contents(path), **data)
    data.update({"content": content})
    if data.get("private") and not getattr(data["user"], "is_authenticated"):
        return ""
    template_file = data.get("output") + ".html"
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
