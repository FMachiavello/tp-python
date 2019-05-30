import EJ4TP2
import unittest


class testEJ4TP2(unittest.TestCase):
    def test_perCirculo(self):
        self.assertEqual(EJ4TP2.perCirculo(5), 31.41516)
        self.assertEqual(EJ4TP2.perCirculo(99), 622.020168)
        self.assertEqual(EJ4TP2.perCirculo(998), 6270.4659360000005)

    def test_perCirculo(self):
        self.assertEqual(EJ4TP2.areaCirculo(5), 246.7280694564)
        self.assertEqual(EJ4TP2.areaCirculo(99), 96727.27234968706)
        self.assertEqual(EJ4TP2.areaCirculo(998), 9829685.763634091)
if __name__ == "__main__":
    unittest.main()
