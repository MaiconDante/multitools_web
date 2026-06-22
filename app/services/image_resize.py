import cv2


def redimensionar_imagem(
    entrada,
    saida,
    largura,
    altura
):

    imagem = cv2.imread(
        str(entrada)
    )

    imagem_redimensionada = cv2.resize(
        imagem,
        (largura, altura)
    )

    cv2.imwrite(
        str(saida),
        imagem_redimensionada
    )
    