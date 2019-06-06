import EJ3
import unittest


class testEJ3(unittest.TestCase):
    def test_contadorDeVocales(self):
        self.assertEqual(EJ3.contDeVocales(""), "")
        self.assertEqual(EJ3.contDeVocales("Shhhhh"), "Nada")
        self.assertEqual(EJ3.contDeVocales("Pssst"), "Nada")
        self.assertEqual(EJ3.contDeVocales("Péron"), "Vocal")
        self.assertEqual(EJ3.contDeVocales("Electroencefalografista"), "Vocal")

    def test_types(self):
        self.assertRaises(TypeError, EJ3.contDeVocales, 5)
        self.assertRaises(TypeError, EJ3.contDeVocales, 5.5)
        self.assertRaises(TypeError, EJ3.contDeVocales, 5j + 5)
        self.assertRaises(TypeError, EJ3.contDeVocales, True)
if __name__ == "__main__":
    unittest.main()
