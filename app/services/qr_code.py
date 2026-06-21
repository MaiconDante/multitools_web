import qrcode


def gerar_qrcode(texto, caminho_saida):

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )

    qr.add_data(texto)

    qr.make(
        fit=True
    )

    imagem = qr.make_image()

    imagem.save(
        caminho_saida
    )
    