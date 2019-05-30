import EJ4
import unittest


class testEJ4(unittest.TestCase):
    def test_pitagoras(self):
        self.assertEqual(EJ4.pitagoras(4, 1, 4, 5, 4, 5), )
        self.assertEqual(EJ4.pitagoras(8), 36)
        self.assertEqual(EJ4.pitagoras(10), 55)
        self.assertEqual(EJ4.pitagoras(1), 1)
if __name__ == "__main__":
    unittest.main()
