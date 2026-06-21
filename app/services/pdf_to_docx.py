from pathlib import Path

import pdfplumber

from docx import Document


def converter_pdf_para_docx(
    pdf_path: Path,
    docx_path: Path
) -> None:

    documento = Document()

    with pdfplumber.open(pdf_path) as pdf:

        for pagina in pdf.pages:

            texto = pagina.extract_text()

            if texto:
                documento.add_paragraph(texto)

    documento.save(docx_path)
    