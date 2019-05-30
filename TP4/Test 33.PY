import EJ3TP2
import unittest


class testEJ3TP2(unittest, TestCase):
    def test_areaRec(self):
        self.assertEqual(EJ3TP2.areaRec(5, 4, 2, 1), 4.0)
if __name__ == "__main__":
    unittest.main()
