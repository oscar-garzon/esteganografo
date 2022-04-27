from random import randint
from typing import List

from PIL import Image
import numpy as np


def convertir_texto_a_binario(texto: str) -> List[str]:
    """Dada una cadena de texto regresa una lista de los valores unicode
    en binario asociado a cada caracter en la cadena.

    Mayúsculas las pasa a minúsculas, remueve acentos, deja espacios en
    blanco si encuentra un caracter inválido.
    """
    texto_en_binario = []
    acentosñ_unicode = {
        "225": 97,
        "233": 101,
        "237": 105,
        "243": 111,
        "250": 117,
        "241": 110,
    }
    texto = texto.lower()
    for caracter in texto:
        valor_unicode_caracter = ord(caracter)
        # remueve acentos
        if str(valor_unicode_caracter) in acentosñ_unicode:
            valor_unicode_caracter = acentosñ_unicode[str(valor_unicode_caracter)]
        # pone espacio en blanco en lugar de caracter inválido
        elif valor_unicode_caracter > 127 or valor_unicode_caracter < 32:
            valor_unicode_caracter = 32

        texto_en_binario.append("{0:08b}".format(valor_unicode_caracter))
    return texto_en_binario


def ocultar_car_bin_en_arr(caracter: str, arr: List[List[int]], indx: int) -> None:
    """Modifica arr para que oculte un caracter en tres pixeles.

    El primer pixel donde se comienza a ocultar 'caracter' es arr[indx].
    caracter debe ser la representación en binario de su valor unicode.
    Se modifica el least significant bit de los tres pixeles(r,g,b).
    Los colores r y g del primer pixel no se modifican.
    """
    for pixel_idx in range(indx, indx + 3):
        for color_idx in range(3):
            if pixel_idx % 3 == 0 and (color_idx == 0 or color_idx == 1):
                continue
            else:
                lsb = int(caracter[3 * (pixel_idx % 3) + color_idx - 1])
            valor = arr[pixel_idx][color_idx]
            arr[pixel_idx][color_idx] = modifica_lsb(valor, lsb)


def ocultar_binario_en_imagen(txt_bin: List[str], img: Image) -> np.ndarray:
    """Oculta en el arreglo de una imagen los valores binarios de una lista.

    Supone que todos los valores están entre 0-127(en binario). Añade '\z'
    en el arreglo de la imagen para señalar el final del texto.
    Lanza Exception cuando el txt_bin no se puede ocultar en la imagen por su
    longitud.
    """
    ancho, alto = img.size
    img_arr_lineal = np.asarray(img, np.uint8).reshape((ancho * alto, 3))

    if ancho * alto < len(txt_bin) * 3 + 6:
        raise Exception("El texto es demasiado largo. No se puede ocultar en imagen")

    for i, caracter in enumerate(txt_bin):
        ocultar_car_bin_en_arr(caracter, img_arr_lineal, 3 * i)

    # Añade '\z' para indicar el fin de texto.
    for i, caracter in enumerate(["01011100", "01111010"]):
        ocultar_car_bin_en_arr(caracter, img_arr_lineal, 3 * len(txt_bin) + 3 * i)

    return img_arr_lineal.reshape((alto, ancho, 3))


def modifica_lsb(num_dec: int, last_bit: int) -> int:
    """Dado un número decimal lo modifica para que su LSB sea igual a last_bit.

    last_bit es 0 ó 1. Modifica el LSB de la representación binaria de num_dec.
    Devuelve la representación decimal de num_dec modificado.
    """
    num_bin = "{0:08b}".format(num_dec)
    num_bin = num_bin[:-1] + str(last_bit)
    num_dec = int(num_bin, 2)
    return num_dec
