import json
import os

import flask
import flask_login

app = flask.Flask(__name__, template_folder="templates")
app.secret_key = os.environ.get("SECRET_KEY", "hello").encode("UTF-8")
login_manager = flask_login.LoginManager()
login_manager.init_app(app)


class User(flask_login.UserMixin):
    id = "admin"


admin = User()


@login_manager.user_loader
def load_user(user_id):
    if user_id == "admin":
        return admin
    return None


# Configuring Jinja
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.errorhandler(404)
def page_not_found(error):
    return render_page("build/404.html")


@app.route("/favicon.ico")
def favicon():
    static = os.path.join(app.root_path, "static")
    return flask.send_from_directory(
        static, "favicon.ico", mimetype="image/vnd.microsoft.icon"
    )


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


@app.route("/boards/<path:url>", methods=["POST"])
@flask_login.login_required
def save_board(url: str = ""):
    boards = flask.request.get_json() or []
    path = source_basepath(url) + ".json"
    if os.path.exists(path):
        old_boards = json.loads(file_contents(path))
        changed = [int(boards[i] != old_boards[i]) for i in range(len(old_boards))]
        if sum(changed) > 1:
            raise ValueError("Boards have changed too much")
    with open(path, "w") as file:
        file.write(json.dumps(clean(boards), separators=(",", ":")))
    return flask.jsonify({"success": True, "boards": boards})


def clean(boards: list) -> list:
    for slide in boards:
        for board in slide:
            for index, path in enumerate(board["paths"]):
                if not path["points"]:
                    del board["paths"][index]
    return boards


@app.route("/boards/<path:url>", methods=["GET"])
def get_board(url: str = ""):
    path = source_basepath(url) + ".json"
    if not path.startswith(".json") and os.path.exists(path):
        return flask.send_file(path)
    flask.abort(404)


@app.route("/")
@app.route("/<path:url>")
def default_route(url: str = ""):
    path = "build/" + source_basepath(url) + ".html"
    if os.path.exists(path):
        return render_page(path)
    flask.abort(404)


def source_basepath(url: str) -> str:
    for suffix in ["", ".html", "index.html"]:
        path = f"build/{url}{suffix}"
        if os.path.exists(path) and not os.path.isdir(path):
            return path[6:-5]
    return ""


def file_contents(path: str) -> str:
    with open(path) as f:
        return f.read()


def render_page(path: str) -> str:
    data = json.loads(file_contents(path.replace(".html", ".json")))
    data["user"] = flask_login.current_user
    content = flask.render_template_string(file_contents(path), **data)
    data.update({"content": content})
    if data.get("private") and not getattr(data["user"], "is_authenticated"):
        return ""
    return flask.render_template("main.html", **data)


if __name__ == "__main__":
    app.run(debug=os.environ.get("ENV", "") != "production")
