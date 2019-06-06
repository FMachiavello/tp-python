import EJ1
import unittest


class testEJ1(unittest.TestCase):
    def test_contraseña(self):
        self.assertEqual(EJ1.contraseña('Luna'), True)
if __name__ == "__main__":
    unittest.main()
