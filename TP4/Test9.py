import EJ9
import unittest


class testEJ9(unittest.TestCase):
    def test_evualaciones(self):
        self.assertEqual(EJ9.evaluaciones(10, 60, 10), "Aprobado")
        self.assertEqual(EJ9.evaluaciones(50, 60, 30), "Aprobado")
        self.assertEqual(EJ9.evaluaciones(50, 60, 10), "Desaprobado")

    def test_types(self):
        self.assertRaises(TypeError, EJ9.evaluaciones, 'a', 'b', 'c')
        self.assertRaises(TypeError, EJ9.evaluaciones, True, False, True)
        self.assertRaises(TypeError, EJ9.evaluaciones, 1 + 5j, 2 + 1j, 5 + 7j)

    def test_valores(self):
        self.assertRaises(ValueError, EJ9.evaluaciones, 0, 0, 0)
        self.assertRaises(ValueError, EJ9.evaluaciones, -1, 101, -1)
if __name__ == "__main__":
    unittest.main()
