import EJ6
import unittest


class testEJ6(unittest.TestCase):
    def test_maxOMin(self):
        self.assertEqual(EJ6.maxOMin(5, 4, 3), (-10.0, -120.0))

    def test_raices(self):
        self.assertEqual(EJ6.raices(-1, -4, 5), (1.0, -5.0))

    def test_intersecccion(self):
        self.assertEqual(EJ6.interseccion(5, 2, 4, 3), (-3.75, -16.75))
if __name__ == "__main__":
    unittest.main()
