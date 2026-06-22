from urllib.parse import quote


def gerar_link_whatsapp(
    telefone: str,
    mensagem: str
) -> str:

    telefone = ''.join(
        filter(str.isdigit, telefone)
    )

    mensagem = quote(mensagem)

    return (
        f"https://wa.me/{telefone}"
        f"?text={mensagem}"
    )
