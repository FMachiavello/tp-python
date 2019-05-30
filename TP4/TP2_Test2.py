import TP2_EJ2
import unittest


class testTP2EJ2(unittest.TestCase):
    def test_areaRectangulo(self):
        self.assertEqual(TP2_EJ2.areaRectangulo(5, 2), 10)
        self.assertEqual(TP2_EJ2.areaRectangulo(3, 7), 21)
        self.assertEqual(TP2_EJ2.areaRectangulo(5, 5), 25)

    def test_negativos(self):
        self.assertRaises(ValueError, TP2_EJ2.areaRectangulo, -5, -5)
        self.assertRaises(ValueError, TP2_EJ2.areaRectangulo, -1, -6)
        self.assertRaises(ValueError, TP2_EJ2.areaRectangulo, -10, -3)

    def test_types(self):
        self.assertRaises(TypeError, TP2_EJ2.areaRectangulo, 'a', 'b')
        self.assertRaises(TypeError, TP2_EJ2.areaRectangulo, True, False)
        self.assertRaises(TypeError, TP2_EJ2.areaRectangulo, 1 + 5j, 1 + 3j)
if __name__ == "__main__":
    unittest.main()
