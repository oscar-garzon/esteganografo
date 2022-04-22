from typing import List

import numpy as np


def develar_texto(arr_img: np.ndarray) -> str:
    """Regresa el texto oculto en un arreglo ."""
    ancho, alto, colores = arr_img.shape
    arr_img_lineal = arr_img.reshape((ancho * alto, colores))

    texto = ''
    for indice in range(0, ancho * alto, 3):
        car_bin = trespixeles_a_car_bin(arr_img_lineal, indice)
        caracter = chr(int(car_bin, 2))
        texto += caracter
        if texto[-2:] == '\z':
            return texto[:-2]


def trespixeles_a_car_bin(arr: List[List[int]], idx: int) -> str:
    """Regresa el valor binario del caracter oculto en arr[idx: idx+3]

    Este método supone que arr es un arreglo lineal de píxeles.
    """
    # el primer dígito siempre va ser cero porque todos los caracteres
    # están entre 0-127
    caracter = '0'
    for pxl in range(3):
        for color in range(3):
            if pxl == 0 and (color == 0 or color == 1):
                continue
            else:
                valor_dec = arr[pxl + idx][color]
                caracter += '{0:08b}'.format(valor_dec)[-1]
    return caracter
