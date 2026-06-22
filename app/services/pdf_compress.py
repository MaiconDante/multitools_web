import fitz


def comprimir_pdf(
    entrada,
    saida
):

    pdf = fitz.open(
        entrada
    )


    novo_pdf = fitz.open()


    for pagina in pdf:

        nova_pagina = novo_pdf.new_page(
            width=pagina.rect.width,
            height=pagina.rect.height
        )


        imagens = pagina.get_images(
            full=True
        )


        if imagens:

            pix = fitz.Pixmap(
                pdf,
                imagens[0][0]
            )


            if pix.alpha:
                pix = fitz.Pixmap(
                    fitz.csRGB,
                    pix
                )


            imagem_bytes = pix.tobytes(
                "jpeg",
                jpg_quality=60
            )


            nova_pagina.insert_image(
                pagina.rect,
                stream=imagem_bytes
            )


        else:

            nova_pagina.show_pdf_page(
                pagina.rect,
                pdf,
                pagina.number
            )


    novo_pdf.save(
        saida,
        garbage=4,
        deflate=True
    )


    pdf.close()

    novo_pdf.close()
    