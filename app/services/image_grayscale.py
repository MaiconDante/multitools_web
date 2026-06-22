import cv2


def converter_para_cinza(
    entrada,
    saida
):

    imagem = cv2.imread(
        str(entrada)
    )

    imagem_cinza = cv2.cvtColor(
        imagem,
        cv2.COLOR_BGR2GRAY
    )

    cv2.imwrite(
        str(saida),
        imagem_cinza
    )
    