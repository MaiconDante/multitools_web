from pathlib import Path

from docx import Document


def converter_rtf_para_docx(arquivo_rtf, arquivo_docx):
    """
    Conversão simples de RTF para DOCX.
    """

    with open(arquivo_rtf, "r", encoding="utf-8", errors="ignore") as arquivo:
        conteudo = arquivo.read()

    documento = Document()
    documento.add_paragraph(conteudo)

    documento.save(arquivo_docx)

    return arquivo_docx
