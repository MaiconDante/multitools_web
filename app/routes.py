from pathlib import Path

from flask import (
    Blueprint,
    render_template,
    request,
    send_file
)

from app.services.rtf_to_docx import (
    converter_rtf_para_docx
)

BASE_DIR = Path(__file__).resolve().parent.parent

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/rtf-docx", methods=["GET", "POST"])
def rtf_docx():

    if request.method == "POST":

        arquivo = request.files.get("arquivo")

        if not arquivo:
            return render_template("rtf_to_docx.html")

        uploads = BASE_DIR / "uploads"
        outputs = BASE_DIR / "outputs"

        uploads.mkdir(exist_ok=True)
        outputs.mkdir(exist_ok=True)

        caminho_rtf = uploads / arquivo.filename

        arquivo.save(caminho_rtf)

        nome_docx = caminho_rtf.stem + ".docx"

        caminho_docx = outputs / nome_docx

        converter_rtf_para_docx(
            caminho_rtf,
            caminho_docx
        )

        print("DOCX:", caminho_docx)
        print("EXISTE:", caminho_docx.exists())

        return send_file(
            str(caminho_docx),
            as_attachment=True
        )

    return render_template("rtf_to_docx.html")

