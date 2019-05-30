import EJ3
import unittest


class testEJ3(unittest.TestCase):
    def test_numTriangular(self):
        self.assertEqual(EJ3.numTriangular(5), 15)
        self.assertEqual(EJ3.numTriangular(8), 36)
        self.assertEqual(EJ3.numTriangular(10), 55)
        self.assertEqual(EJ3.numTriangular(1), 1)

    def test_isnumeric_numTriangular(self):
        self.assertEqual(EJ3.isnumeric(1), True)
        self.assertEqual(EJ3.isnumeric('a'), False)
        self.assertEqual(EJ3.numTriangular('a'), "Todo mal")
        self.assertEqual(EJ3.numTriangular(5), 15)
if __name__ == "__main__":
    unittest.main()
