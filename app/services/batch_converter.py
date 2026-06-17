from pathlib import Path
from zipfile import ZipFile

from app.services.rtf_to_docx import converter_rtf_para_docx


def converter_lote_rtf_para_docx(
    arquivos,
    pasta_uploads,
    pasta_outputs
):
    arquivos_convertidos = []

    for arquivo in arquivos:

        caminho_rtf = pasta_uploads / arquivo.filename

        arquivo.save(caminho_rtf)

        nome_docx = Path(arquivo.filename).stem + ".docx"

        caminho_docx = pasta_outputs / nome_docx

        converter_rtf_para_docx(
            caminho_rtf,
            caminho_docx
        )

        arquivos_convertidos.append(caminho_docx)

    zip_path = pasta_outputs / "resultado.zip"

    with ZipFile(zip_path, "w") as zip_file:

        for arquivo_convertido in arquivos_convertidos:
            zip_file.write(
                arquivo_convertido,
                arquivo_convertido.name
            )

    return zip_path
