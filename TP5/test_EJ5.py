import EJ5
import unittest


class testEJ5(unittest.TestCase):
    def test_primeraLetra(self):
        self.assertEqual(EJ5.primeraLetra("Hagamos algo por favor"), "OK (a)")
        self.assertEqual(EJ5.primeraLetra("Ahre loco"), "OK (a)")
        self.assertEqual(EJ5.primeraLetra("Cara de Aristoteles"), "OK (a)")

    def test_letraMayuscula(self):
        self.assertEqual(EJ5.letraMayuscula("croissant"), "OK (b)")
        self.assertEqual(EJ5.letraMayuscula("ahre loco"), "OK (b)")
        self.assertEqual(EJ5.letraMayuscula("cara de aristoteles"), "OK (b)")

    def test_palabrasConA(self):
        self.assertEqual(EJ5.palabrasConA("hagamos algo por favor"), "OK (c)")
        self.assertEqual(EJ5.palabrasConA("ahre loco"), "OK (c)")
        self.assertEqual(EJ5.palabrasConA("cara de aristoteles"), "OK (c)")
        self.assertEqual(EJ5.palabrasConA("Caramelo"), "Fail (c)")
        self.assertEqual(EJ5.palabrasConA("Perro"), "Fail (c)")
        self.assertEqual(EJ5.palabrasConA("Dinosaurio"), "Fail (c)")

    def test_types(self):
        self.assertRaises(TypeError, EJ5.primeraLetra, 5)
        self.assertRaises(TypeError, EJ5.primeraLetra, 5.5)
        self.assertRaises(TypeError, EJ5.primeraLetra, True)
        self.assertRaises(TypeError, EJ5.primeraLetra, 5j + 1)
        self.assertRaises(TypeError, EJ5.letraMayuscula, 5)
        self.assertRaises(TypeError, EJ5.letraMayuscula, 5.5)
        self.assertRaises(TypeError, EJ5.letraMayuscula, True)
        self.assertRaises(TypeError, EJ5.letraMayuscula, 5j + 1)
        self.assertRaises(TypeError, EJ5.palabrasConA, 5)
        self.assertRaises(TypeError, EJ5.palabrasConA, 5.5)
        self.assertRaises(TypeError, EJ5.palabrasConA, True)
        self.assertRaises(TypeError, EJ5.palabrasConA, 5j + 1)
if __name__ == "__main__":
    unittest.main()
