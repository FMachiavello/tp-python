import EJ7
import unittest


class testEJ7(unittest.TestCase):
    def test_dias(self):
        self.assertEqual(EJ7.dias(1), "Lunes")
        self.assertEqual(EJ7.dias(5), "Viernes")
        self.assertEqual(EJ7.dias(8), "Lunes")
if __name__ == "__main__":
    unittest.main()
