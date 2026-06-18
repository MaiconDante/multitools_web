from pathlib import Path

def limpar_pasta(caminho_pasta):
    pasta = Path(caminho_pasta)

    if not pasta.exists():
        return

    for arquivo in pasta.iterdir():

        if arquivo.is_file():

            try:
                arquivo.unlink()

            except Exception:
                pass
