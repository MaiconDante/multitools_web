import cv2
import numpy as np


def ordenar_pontos(pontos):

    pontos = pontos.reshape(4, 2)

    resultado = np.zeros((4, 2), dtype="float32")


    soma = pontos.sum(axis=1)

    resultado[0] = pontos[np.argmin(soma)]
    resultado[2] = pontos[np.argmax(soma)]


    diferenca = np.diff(pontos, axis=1)

    resultado[1] = pontos[np.argmin(diferenca)]
    resultado[3] = pontos[np.argmax(diferenca)]


    return resultado



def endireitar_documento(
    entrada,
    saida
):

    imagem = cv2.imread(
        str(entrada)
    )


    original = imagem.copy()


    cinza = cv2.cvtColor(
        imagem,
        cv2.COLOR_BGR2GRAY
    )


    desfoque = cv2.GaussianBlur(
        cinza,
        (5,5),
        0
    )


    bordas = cv2.Canny(
        desfoque,
        75,
        200
    )


    contornos, _ = cv2.findContours(
        bordas,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )


    contornos = sorted(
        contornos,
        key=cv2.contourArea,
        reverse=True
    )


    documento = None


    for c in contornos:

        perimetro = cv2.arcLength(
            c,
            True
        )


        aproximacao = cv2.approxPolyDP(
            c,
            0.02 * perimetro,
            True
        )


        if len(aproximacao) == 4:

            documento = aproximacao

            break



    if documento is None:

        cv2.imwrite(
            str(saida),
            original
        )

        return



    pontos = ordenar_pontos(
        documento
    )


    largura = 1000
    altura = 1400


    destino = np.array(
        [
            [0,0],
            [largura-1,0],
            [largura-1,altura-1],
            [0,altura-1]
        ],
        dtype="float32"
    )


    matriz = cv2.getPerspectiveTransform(
        pontos,
        destino
    )


    corrigida = cv2.warpPerspective(
        original,
        matriz,
        (largura, altura)
    )


    cv2.imwrite(
        str(saida),
        corrigida
    )
    