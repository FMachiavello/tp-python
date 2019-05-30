import TP2_EJ1
import unittest


class testTP2EJ1(unittest.TestCase):
    def test_perRectangulo(self):
        self.assertEqual(TP2_EJ1.perRectangulo(5, 2), 14)
        self.assertEqual(TP2_EJ1.perRectangulo(1, 1), 4)
        self.assertEqual(TP2_EJ1.perRectangulo(0.5, 1), 3)

    def test_negativos(self):
        self.assertRaises(ValueError, TP2_EJ1.perRectangulo, -5, -1)
        self.assertRaises(ValueError, TP2_EJ1.perRectangulo, -6, -2)
        self.assertRaises(ValueError, TP2_EJ1.perRectangulo, -10, -3)

    def test_types(self):
        self.assertRaises(TypeError, TP2_EJ1.perRectangulo, 'a', 'b')
        self.assertRaises(TypeError, TP2_EJ1.perRectangulo, True, False)
        self.assertRaises(TypeError, TP2_EJ1.perRectangulo, 1 + 5j, 1 + 9j)
if __name__ == "__main__":
    unittest.main()
