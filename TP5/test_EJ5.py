import EJ5
import unittest


class testEJ5(unittest.TestCase):
    def test_filtro(self):
        self.assertEqual(EJ5.filtro("Caramelo"), "Fail (c)")
        self.assertEqual(EJ5.filtro("Perro"), "Fail (c)")
        self.assertEqual(EJ5.filtro("Dinosaurio"), "Fail (c)")
        self.assertEqual(EJ5.filtro("Hagamos algo por favor"), "OK")
        self.assertEqual(EJ5.filtro("Ahre loco"), "OK")
        self.assertEqual(EJ5.filtro("Cara de Aristoteles"), "OK")

    def test_types(self):
        self.assertRaises(TypeError, EJ5.filtro, 5)
        self.assertRaises(TypeError, EJ5.filtro, 5.5)
        self.assertRaises(TypeError, EJ5.filtro, True)
        self.assertRaises(TypeError, EJ5.filtro, 5j + 1)
if __name__ == "__main__":
    unittest.main()
