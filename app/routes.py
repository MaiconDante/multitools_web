from flask import Blueprint, render_template

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/rtf-docx")
def rtf_docx():
    return render_template("rtf_to_docx.html")
