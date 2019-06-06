import EJ3
import unittest


class testEJ3(unittest.TestCase):
    def test_numTriangular(self):
        """Prueba si la función dias funciona correctamente"""
        self.assertEqual(EJ3.numTriangular(5), ([1, 2, 3, 4, 5],
                                                [1.0, 3.0, 6.0, 10.0, 15.0]))
        self.assertEqual(EJ3.numTriangular(8), ([1, 2, 3, 4, 5, 6, 7, 8],
                                                [1.0, 3.0, 6.0, 10.0, 15.0,
                                                21.0, 28.0, 36.0]))
        self.assertEqual(EJ3.numTriangular(10), ([1, 2, 3, 4, 5, 6, 7, 8, 9,
                                                 10], [1.0, 3.0, 6.0, 10.0,
                                                 15.0, 21.0, 28.0, 36.0,
                                                 45.0, 55.0]))
        self.assertEqual(EJ3.numTriangular(1),  ([1], [1.0]))

<<<<<<< HEAD
    def test_isnumeric_numTriangular(self):
        self.assertEqual(EJ3.isnumeric(1), True)
        self.assertEqual(EJ3.isnumeric('a'), False)
        self.assertEqual(EJ3.numTriangular('a'), "Todo mal")
        self.assertEqual(EJ3.numTriangular(5), 15)
=======
    def test_types(self):
        """Prueba distintos valores que la función no acepta"""
        self.assertRaises(TypeError, EJ3.numTriangular, 'a')
        self.assertRaises(TypeError, EJ3.numTriangular, True)
        self.assertRaises(TypeError, EJ3.numTriangular, 1 + 5j)
>>>>>>> b82af1983a3b74358863fe88ab4b77db971b7afa
if __name__ == "__main__":
    unittest.main()
