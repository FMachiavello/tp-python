import EJ7
import unittest


class testEJ7(unittest.TestCase):
    def test_EJ7(self):
        """Prueba si la función EJ7 funciona correctamente"""
        self.assertEqual(EJ7.dias(1), 1)
        self.assertEqual(EJ7.dias(5), 5)
        self.assertEqual(EJ7.dias(8), 1)
        self.assertEqual(EJ7.dias(50), 1)

    def test_types(self):
        """Prueba distintos valores que la función no acepta"""
        self.assertRaises(TypeError, EJ7.dias, 'a')
        self.assertRaises(TypeError, EJ7.dias, True)
        self.assertRaises(TypeError, EJ7.dias, 1 + 5j)
        self.assertRaises(TypeError, EJ7.dias, 2.5)

    def test_rango_valores(self):
        """Prueba distintos valores que esten fuera del rango establecido"""
        self.assertRaises(ValueError, EJ7.dias, 0)
        self.assertRaises(ValueError, EJ7.dias, 367)
        self.assertRaises(ValueError, EJ7.dias, -2)
if __name__ == "__main__":
    unittest.main()
