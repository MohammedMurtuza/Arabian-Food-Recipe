import os
from flask import Flask
from flask.helpers import send_from_directory

app = Flask(__name__)


@app.route("/", defaults={'path': ''})
@app.route("/<path:path>")
def main(path):
    path = path or "Food.html"
    return send_from_directory("template", path)


if __name__ == "__main__":
    app.run("0.0.0.0", os.getenv("PORT"), debug=False)
