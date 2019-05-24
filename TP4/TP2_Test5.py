import TP2_EJ5
import unittest


class testTP2EJ5(unittest.TestCase):
    def test_pruebaNumeros(self):
        self.assertEqual(TP2_EJ5.volEsfera(1), 4.19)
        self.assertEqual(TP2_EJ5.volEsfera(50), 523598.78)
        self.assertEqual(TP2_EJ5.volEsfera(500), 523598775.6)
        self.assertEqual(TP2_EJ5.volEsfera(1.5), 14.14)

    def test_types(self):
        self.assertRaises(TypeError, TP2_EJ5.volEsfera, 'a')
        self.assertRaises(TypeError, TP2_EJ5.volEsfera, True)
        self.assertRaises(TypeError, TP2_EJ5.volEsfera, 1 + 5j)

    def test_valores(self):
        self.assertRaises(ValueError, TP2_EJ5.volEsfera, -50)
        self.assertRaises(ValueError, TP2_EJ5.volEsfera, '')
        self.assertRaises(ValueError, TP2_EJ5.volEsfera, -1)

if __name__ == "__main__":
    unittest.main()
