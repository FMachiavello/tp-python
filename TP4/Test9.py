import EJ9
import unittest


class testEJ9(unittest.TestCase):
    def test_evualaciones(self):
        self.assertEqual(EJ9.evaluaciones(10, 60, 10), "Aprobado")
        self.assertEqual(EJ9.evaluaciones(50, 60, 30), "Aprobado")
        self.assertEqual(EJ9.evaluaciones(50, 60, 10), "Desaprobado")
if __name__ == "__main__":
    unittest.main()
