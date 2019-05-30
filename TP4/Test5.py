import EJ5
import unittest


class testEJ5(unittest.TestCase):
    def test_matrizIdentidad(self):
        self.assertEqual(EJ5.MatrizIdentidad(5), ([[1, 0, 0, 0, 0],
                                                   [0, 1, 0, 0, 0],
                                                   [0, 0, 1, 0, 0],
                                                   [0, 0, 0, 1, 0],
                                                   [0, 0, 0, 0, 1]]))
        self.assertEqual(EJ5.MatrizIdentidad(6), ([[1, 0, 0, 0, 0, 0],
                                                   [0, 1, 0, 0, 0, 0],
                                                   [0, 0, 1, 0, 0, 0],
                                                   [0, 0, 0, 1, 0, 0],
                                                   [0, 0, 0, 0, 1, 0],
                                                   [0, 0, 0, 0, 0, 1]]))
if __name__ == "__main__":
    unittest.main()
