import os
import sys
import unittest

sys.path.append(os.getcwd())

from src import main

class Tests(unittest.TestCase):
    def test_main(self):
        """ Test de la funcion principal
        """
        def llamar_funciones(texto_a_ocultar, txt_esperado):
            with open('textos/texto.txt', 'w') as archivo:
                archivo.write(texto_a_ocultar)
            main.ocultar_texto_en_imagen(
                'texto.txt', 'fac.png', 'fac_mod.png'
            )
            main.develar_texto_en_imagen(
                'fac_mod.png', 'txt_develado.txt'
            )
            with open('textos/txt_develado.txt') as txt:
                self.assertEqual(txt.read(), txt_esperado)

        pruebas = [
            (
                '¡Y se me emborrachó hasta el alma!',
                ' y se me emborracho hasta el alma!',
            ),
            ('Tengŋ s→gnøs raros.', 'teng  s gn s raros.'),
        ]
        for prueba in pruebas:
            texto_a_ocultar = prueba[0]
            txt_esperado = prueba[1]
            llamar_funciones(texto_a_ocultar, txt_esperado)

    def test_texto_muy_largo(self):
        s = ' '
        s = s.join([str(i) for i in range(1228803)])
        with open('textos/texto_muy_largo.txt', 'w') as archivo:
            archivo.write(s)
        self.assertRaises(Exception, main.ocultar_texto_en_imagen, ['texto_muy_largo.txt', 'fac.png', 'fac_mod.png'])

    def correr_tests():
        unittest.main()

# __pdoc__ = {'Tests' : False}

if __name__ == '__main__':
    unittest.main()
