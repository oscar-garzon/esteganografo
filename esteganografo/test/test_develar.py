import os
import sys
import unittest

from PIL import Image
import numpy as np

sys.path.append(os.getcwd())

from src import develar, ocultar


class Tests(unittest.TestCase):
    def test_trespixeles_a_car_bin(self):
        car_devuelto = develar.trespixeles_a_car_bin(
            [[14, 14, 15], [21, 20, 20], [30, 30, 31]], 0
        )
        self.assertEqual(car_devuelto, "{0:08b}".format(ord("a")))
        car_devuelto = develar.trespixeles_a_car_bin(
            [[16, 16, 17], [13, 13, 12], [16, 16, 16]], 0
        )
        self.assertEqual(car_devuelto, "{0:08b}".format(ord("p")))


if __name__ == "__main__":
    unittest.main()
