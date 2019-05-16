import EJ8
import unittest


class testEJ8(unittest.TestCase):
    def test_numRomanos(self):
        self.assertEqual(EJ8.numRomanos(1000000), "M//")
        self.assertEqual(EJ8.numRomanos(5), "V")
        self.assertEqual(EJ8.numRomanos(10), "X")
if __name__ == "__main__":
    unittest.main()
