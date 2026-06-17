from app.services.rtf_to_docx import converter_rtf_para_docx

converter_rtf_para_docx(
    "testes/exemplo.rtf",
    "testes/exemplo.docx"
)

print("Conversão concluída.")
