import EJ1
import unittest


class testEJ1(unittest.TestCase):
    maxDiff = None

    def test_milPalabras(self):
        self.assertEqual(EJ1.milPalabras("hola"), 1000)
if __name__ == "__main__":
    unittest.main()
