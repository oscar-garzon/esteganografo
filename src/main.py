import os
from sys import argv, exit, path

from PIL import Image
import numpy as np

path.append(os.getcwd() + "/src")

import ocultar, develar


def ocultar_texto_en_imagen(
    archivo_texto: str, img_original: str, nombre_img_modificada: str
) -> None:
    """Oculta el contenido de archivo_texto en img_original y lo guarda en
    el sistema como ${nombre_img_modificada}.png
    """

    with open(f"textos/{archivo_texto}") as at:
        texto = at.read().strip()
        img = Image.open(f"imagenes/{img_original}")
    txt_binario = ocultar.convertir_texto_a_binario(texto)
    arr_modificado = ocultar.ocultar_binario_en_imagen(txt_binario, img)
    img_final = Image.fromarray(arr_modificado)
    img_final.save(f"imagenes/{nombre_img_modificada}", format="png")


def develar_texto_en_imagen(img: str, nombre_texto: str) -> None:
    """Devela el texto oculto en img y lo guarda en el sistema como
    ${nombre_texto}.txt
    """
    try:
        img = Image.open(f"imagenes/{img}")
    except OSError:
        print("Imagen no encontrada")
    texto_develado = develar.develar_texto(np.asarray(img, np.uint8))
    with open(f"textos/{nombre_texto}", "w") as archivo:
        archivo.write(texto_develado)


if __name__ == "__main__":

    def uso():
        print(
            "Uso:\n Ocultar: python src/main.py h [archivo con texto(.txt) a ocultar] [imagen(.png)] [nombre de imagen con texto oculto (.png)]"
        )
        print(
            " Develar: python src/main.py u [imagen(.png) con texto oculto] [nombre de archivo(.txt) para guardar el texto]"
        )
        exit()

    if argv[1] == "h":
        if len(argv) != 5:
            uso()
        if argv[2][-3:] != "txt" or argv[3][-3:] != "png" or argv[4][-3:] != "png":
            uso()
        try:
            ocultar_texto_en_imagen(argv[2], argv[3], argv[4])
        except FileNotFoundError:
            print("Imagen o archivo de texto no encontrados")
        except Exception as e:
            print(e)
    elif argv[1] == "u":
        if len(argv) != 4:
            uso()
        if argv[2][-3:] != "png" or argv[3][-3:] != "txt":
            uso()
        develar_texto_en_imagen(argv[2], argv[3])
