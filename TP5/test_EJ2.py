import EJ2
import unittest


class testEJ2(unittest.TestCase):
    def test_contadorDeLetras(self):
        self.assertEqual(EJ2.contDeLetras(""), "")
        self.assertEqual(EJ2.contDeLetras("Monitor"), "Nada")
        self.assertEqual(EJ2.contDeLetras("Tiburon"), "Nada")
        self.assertEqual(EJ2.contDeLetras("Péron"), "E")
        self.assertEqual(EJ2.contDeLetras("Luna"), "A")
        self.assertEqual(EJ2.contDeLetras("Mamífero"), "Igual")

    def test_types(self):
        self.assertRaises(TypeError, EJ2.contDeLetras, 5)
        self.assertRaises(TypeError, EJ2.contDeLetras, 5.5)
        self.assertRaises(TypeError, EJ2.contDeLetras, 5j + 5)
        self.assertRaises(TypeError, EJ2.contDeLetras, True)
if __name__ == "__main__":
    unittest.main()
