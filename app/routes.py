from pathlib import Path

from flask import (
    Blueprint,
    render_template,
    request,
    send_file,
)
from app.services.rtf_to_docx import (
    converter_rtf_para_docx
)

from app.services.batch_converter import (
    converter_lote_rtf_para_docx
)

from app.services.pdf_to_docx import (
    converter_pdf_para_docx
)

from app.services.qr_code import ( 
    gerar_qrcode
)

from app.services.whatsapp_link import (
    gerar_link_whatsapp
)

from app.services.image_grayscale import (
    converter_para_cinza
)

from app.services.image_resize import (
    redimensionar_imagem
)

from app.services.file_cleanup import limpar_pasta

BASE_DIR = Path(__file__).resolve().parent.parent

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/rtf-docx", methods=["GET", "POST"])
def rtf_docx():

    if request.method == "POST":

        uploads = BASE_DIR / "uploads"
        outputs = BASE_DIR / "outputs"

        uploads.mkdir(exist_ok=True)
        outputs.mkdir(exist_ok=True)

        limpar_pasta(uploads)
        limpar_pasta(outputs)

        arquivo = request.files.get("arquivo")

        caminho_rtf = uploads / arquivo.filename

        arquivo.save(caminho_rtf)

        nome_docx = caminho_rtf.stem + ".docx"

        caminho_docx = outputs / nome_docx

        converter_rtf_para_docx(
            caminho_rtf,
            caminho_docx
        )

        return send_file(
            str(caminho_docx),
            as_attachment=True
        )

    return render_template("rtf_to_docx.html")


@main.route(
    "/rtf-docx-lote",
    methods=["GET", "POST"]
)
def rtf_docx_lote():

    if request.method == "POST":

        uploads = BASE_DIR / "uploads"
        outputs = BASE_DIR / "outputs"

        uploads.mkdir(exist_ok=True)
        outputs.mkdir(exist_ok=True)

        limpar_pasta(uploads)
        limpar_pasta(outputs)

        arquivos = request.files.getlist("arquivos")

        if not arquivos:
            return render_template(
                "rtf_to_docx_batch.html"
            )

        zip_path = converter_lote_rtf_para_docx(
            arquivos,
            uploads,
            outputs
        )

        return send_file(
            str(zip_path),
            as_attachment=True
        )

    return render_template(
        "rtf_to_docx_batch.html"
    )

@main.route(
    "/qr-code",
    methods=["GET", "POST"]
)
def qr_code():

    if request.method == "POST":

        outputs = BASE_DIR / "outputs"

        outputs.mkdir(
            exist_ok=True
        )

        limpar_pasta(outputs)


        texto = request.form["texto"]


        arquivo = outputs / "qrcode.png"


        gerar_qrcode(
            texto,
            arquivo
        )


        return send_file(
            arquivo,
            as_attachment=True
        )


    return render_template(
        "qr_code.html"
    )

@main.route(
    "/pdf-docx",
    methods=["GET", "POST"]
)
def pdf_docx():

    if request.method == "POST":

        uploads = BASE_DIR / "uploads"
        outputs = BASE_DIR / "outputs"

        uploads.mkdir(exist_ok=True)
        outputs.mkdir(exist_ok=True)

        limpar_pasta(uploads)
        limpar_pasta(outputs)

        arquivo = request.files["arquivo"]

        pdf_path = uploads / arquivo.filename

        arquivo.save(pdf_path)

        docx_path = outputs / (
            pdf_path.stem + ".docx"
        )

        converter_pdf_para_docx(
            pdf_path,
            docx_path
        )

        return send_file(
            docx_path,
            as_attachment=True
        )

    return render_template(
        "pdf_to_docx.html"
    )


@main.route("/pdf-ocr-docx")
def pdf_ocr_docx():
    return render_template(
        "em_desenvolvimento.html"
    )

@main.route(
    "/whatsapp-link",
    methods=["GET", "POST"]
)
def whatsapp_link():

    link = None

    if request.method == "POST":

        telefone = request.form["telefone"]

        mensagem = request.form["mensagem"]

        link = gerar_link_whatsapp(
            telefone,
            mensagem
        )

    return render_template(
        "whatsapp_link.html",
        link=link
    )

@main.route(
    "/image-grayscale",
    methods=["GET", "POST"]
)
def image_grayscale():

    if request.method == "POST":

        uploads = BASE_DIR / "uploads"
        outputs = BASE_DIR / "outputs"

        uploads.mkdir(exist_ok=True)
        outputs.mkdir(exist_ok=True)

        limpar_pasta(uploads)
        limpar_pasta(outputs)

        arquivo = request.files["arquivo"]

        imagem_entrada = uploads / arquivo.filename

        arquivo.save(imagem_entrada)

        imagem_saida = outputs / (
            imagem_entrada.stem + "_cinza.jpg"
        )

        converter_para_cinza(
            imagem_entrada,
            imagem_saida
        )

        return send_file(
            imagem_saida,
            as_attachment=True
        )

    return render_template(
        "image_grayscale.html"
    )

@main.route(
    "/image-resize",
    methods=["GET", "POST"]
)
def image_resize():

    if request.method == "POST":

        uploads = BASE_DIR / "uploads"
        outputs = BASE_DIR / "outputs"

        uploads.mkdir(exist_ok=True)
        outputs.mkdir(exist_ok=True)

        limpar_pasta(uploads)
        limpar_pasta(outputs)

        arquivo = request.files["arquivo"]

        largura = int(
            request.form["largura"]
        )

        altura = int(
            request.form["altura"]
        )

        imagem_entrada = uploads / arquivo.filename

        arquivo.save(
            imagem_entrada
        )

        imagem_saida = outputs / (
            imagem_entrada.stem +
            "_resize.jpg"
        )

        redimensionar_imagem(
            imagem_entrada,
            imagem_saida,
            largura,
            altura
        )

        return send_file(
            imagem_saida,
            as_attachment=True
        )

    return render_template(
        "image_resize.html"
    )
