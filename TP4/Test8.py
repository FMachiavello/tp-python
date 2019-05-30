import EJ8
import unittest


class testEJ8(unittest.TestCase):
    def test_numRomanos(self):
        """Prueba si la función numRomanos funciona correctamente"""
        self.assertEqual(EJ8.numRomanos(1000000), "M//")
        self.assertEqual(EJ8.numRomanos(5), "V")
        self.assertEqual(EJ8.numRomanos(10), "X")

    def test_types(self):
        """Prueba distintos valores que la función no acepta"""
        self.assertRaises(TypeError, EJ8.numRomanos, 'a')
        self.assertRaises(TypeError, EJ8.numRomanos, True)
        self.assertRaises(TypeError, EJ8.numRomanos, 1 + 8j)
        self.assertRaises(TypeError, EJ8.numRomanos, 2.5)

    def test_rango_valores(self):
        """Prueba distintos valores que esten fuera del rango establecido"""
        self.assertRaises(ValueError, EJ8.numRomanos, 0)
        self.assertRaises(ValueError, EJ8.numRomanos, 2000000)
        self.assertRaises(ValueError, EJ8.numRomanos, -1)
if __name__ == "__main__":
    unittest.main()
