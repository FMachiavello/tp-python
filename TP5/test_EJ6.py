import ej6
import unittest


class testEJ6(unittest.TestCase):
    def test_SacarConsonantes(self):
        self.assertEqual(ej6.sacarConsonantes("hola"), "hl")
        self.assertEqual(ej6.sacarConsonantes("aaayaaayayayaaay"), "yyyyy")

    def test_types(self):
        self.assertRaises(TypeError, ej6.sacarConsonantes, 5)
        self.assertRaises(TypeError, ej6.sacarConsonantes, True)
        self.assertRaises(TypeError, ej6.sacarConsonantes, 8.6)
        self.assertRaises(TypeError, ej6.sacarConsonantes, False)
        self.assertRaises(TypeError, ej6.sacarVocales, False)
        self.assertRaises(TypeError, ej6.sacarVocales, True)
        self.assertRaises(TypeError, ej6.sacarVocales, 8.5)
        self.assertRaises(TypeError, ej6.sacarVocales, 4)
        self.assertRaises(TypeError, ej6.adelantarVocal, False)
        self.assertRaises(TypeError, ej6.adelantarVocal, True)
        self.assertRaises(TypeError, ej6.adelantarVocal, 8.5)
        self.assertRaises(TypeError, ej6.esPalindromo, False)
        self.assertRaises(TypeError, ej6.esPalindromo, True)
        self.assertRaises(TypeError, ej6.esPalindromo, 8.5)

    def test_SacarVocales(self):
        self.assertEqual(ej6.sacarVocales("hola"), "oa")
        self.assertEqual(ej6.sacarVocales("aaayyayayaay"), "aaaaaaa")

    def test_adelantarVocales(self):
        self.assertEqual(ej6.adelantarVocal("hola"), "hule")
        self.assertEqual(ej6.adelantarVocal("casa"), "cese")

    def test_esPalindromo(self):
        self.assertEqual(ej6.esPalindromo("neuquen"), True)
        self.assertEqual(ej6.esPalindromo("fsociety"), False)
        self.assertEqual(ej6.esPalindromo("teemo"), False)


if __name__ == "__main__":
    unittest.main()
