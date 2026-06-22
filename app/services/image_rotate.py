import cv2


def rotacionar_imagem(
    entrada,
    saida,
    angulo
):

    imagem = cv2.imread(
        str(entrada)
    )

    altura, largura = imagem.shape[:2]

    centro = (
        largura // 2,
        altura // 2
    )

    matriz = cv2.getRotationMatrix2D(
        centro,
        angulo,
        1.0
    )

    imagem_rotacionada = cv2.warpAffine(
        imagem,
        matriz,
        (largura, altura)
    )

    cv2.imwrite(
        str(saida),
        imagem_rotacionada
    )
    