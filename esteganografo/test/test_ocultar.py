import os
import sys
import unittest

from PIL import Image
import numpy as np

sys.path.append(os.getcwd())

from src import ocultar


class Tests(unittest.TestCase):
    def test_convertir_texto_a_binario(self):
        s = "hola bebe!"
        s_acentos_mayuscula = "Hola bebé!"
        simbolos_invalidos = "æ es inv@lido y tæmßien"
        simb_sencilla = "æxßá"
        s_unicode = [
            "01101000",
            "01101111",
            "01101100",
            "01100001",
            "00100000",
            "01100010",
            "01100101",
            "01100010",
            "01100101",
            "00100001",
        ]
        simbolos_invalidos_unicode = [
            "00100000",
            "00100000",
            "01100101",
            "01110011",
            "00100000",
            "01101001",
            "01101110",
            "01110110",
            "01000000",
            "01101100",
            "01101001",
            "01100100",
            "01101111",
            "00100000",
            "01111001",
            "00100000",
            "01110100",
            "00100000",
            "01101101",
            "00100000",
            "01101001",
            "01100101",
            "01101110",
        ]
        simb_sencilla_unicode = [
            "00100000",
            "01111000",
            "00100000",
            "01100001",
        ]
        self.assertListEqual(ocultar.convertir_texto_a_binario(s), s_unicode)
        self.assertListEqual(
            ocultar.convertir_texto_a_binario(s_acentos_mayuscula), s_unicode
        )
        self.assertListEqual(
            ocultar.convertir_texto_a_binario(simbolos_invalidos),
            simbolos_invalidos_unicode,
        )
        self.assertListEqual(
            ocultar.convertir_texto_a_binario(simb_sencilla), simb_sencilla_unicode,
        )

    def test_modifica_lsb(self):
        self.assertEqual(ocultar.modifica_lsb(15, 0), 14)
        self.assertEqual(ocultar.modifica_lsb(15, 1), 15)
        self.assertEqual(ocultar.modifica_lsb(0, 1), 1)
        self.assertEqual(ocultar.modifica_lsb(0, 0), 0)

    def test_ocultar_car_bin_en_arr(self):
        arr = [
            [12, 12, 12],
            [14, 14, 14],
            [15, 15, 15],
            [24, 24, 24],
            [36, 36, 36],
            [37, 37, 37],
            [16, 16, 16],
        ]
        ocultar.ocultar_car_bin_en_arr("01100001", arr, 3)
        arr_esperado = [
            [12, 12, 12],
            [14, 14, 14],
            [15, 15, 15],
            [24, 24, 25],
            [37, 36, 36],
            [36, 36, 37],
            [16, 16, 16],
        ]
        self.assertListEqual(arr, arr_esperado)

    def test_ocultar_binario_en_imagen(self):
        img = Image.open("imagenes/fac.png")
        ancho, alto = img.size

        s = " "
        s = s.join([str(i) for i in range(ancho * alto + 3)])
        txt_bin = ocultar.convertir_texto_a_binario(s)
        self.assertRaises(Exception, ocultar.ocultar_binario_en_imagen, [txt_bin, img])

        txt_bin = ocultar.convertir_texto_a_binario("a")
        arr_esperado = [[15, 15, 15], [21, 20, 20], [30, 30, 31]]
        arr_obtenido = (
            ocultar.ocultar_binario_en_imagen(txt_bin, img)
            .reshape((ancho * alto, 3))
            .tolist()[:3]
        )
        self.assertListEqual(arr_obtenido, arr_esperado)

        txt_bin = ocultar.convertir_texto_a_binario("Pæpá")
        arr_esperado = [
            [15, 15, 15],
            [21, 21, 20],
            [30, 30, 30],
            [32, 32, 32],
            [19, 18, 18],
            [12, 12, 12],
            [16, 16, 17],
            [13, 13, 12],
            [16, 16, 16],
            [19, 19, 19],
            [23, 22, 22],
            [26, 26, 27],
            [26, 26, 27],
            [22, 23, 23],
            [19, 18, 18],
            [15, 15, 15],
            [19, 19, 19],
            [22, 23, 22],
        ]
        arr_obtenido = (
            ocultar.ocultar_binario_en_imagen(txt_bin, img)
            .reshape((ancho * alto, 3))
            .tolist()[:18]
        )
        self.assertListEqual(arr_obtenido, arr_esperado)


if __name__ == "__main__":
    unittest.main()
