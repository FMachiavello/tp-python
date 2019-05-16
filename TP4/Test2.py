import EJ2
import unittest


class testEJ2(unittest.TestCase):
    def test_Domino(self):
        self.assertEqual(EJ2.domino(), 28)
if __name__ == "__main__":
    unittest.main()