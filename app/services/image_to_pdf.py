from PIL import Image


def imagem_para_pdf(
    entrada,
    saida
):

    imagem = Image.open(
        entrada
    )


    if imagem.mode != "RGB":

        imagem = imagem.convert(
            "RGB"
        )


    imagem.save(
        saida,
        "PDF"
    )
    