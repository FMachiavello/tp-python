import TP2_EJ4
import unittest


class testTP2EJ4(unittest.TestCase):
    def test_perCirculo(self):
        self.assertEqual(TP2_EJ4.perCirculo(5), 31.41516)
        self.assertEqual(TP2_EJ4.perCirculo(99), 622.020168)
        self.assertEqual(TP2_EJ4.perCirculo(998), 6270.4659360000005)

    def test_perCirculo(self):
        self.assertEqual(TP2_EJ4.areaCirculo(5), 246.7280694564)
        self.assertEqual(TP2_EJ4.areaCirculo(99), 96727.27234968706)
        self.assertEqual(TP2_EJ4.areaCirculo(998), 9829685.763634091)

    def test_typePC(self):
        self.assertRaises(TypeError, TP2_EJ4.perCirculo, 'a')
        self.assertRaises(TypeError, TP2_EJ4.perCirculo, True)
        self.assertRaises(TypeError, TP2_EJ4.perCirculo, 1 + 5j)

    def test_typeAC(self):
        self.assertRaises(TypeError, TP2_EJ4.areaCirculo, 'a')
        self.assertRaises(TypeError, TP2_EJ4.areaCirculo, True)
        self.assertRaises(TypeError, TP2_EJ4.areaCirculo, 1 + 5j)

    def test_valoresPC(self):
        self.assertRaises(ValueError, TP2_EJ4.perCirculo, -5)
        self.assertRaises(ValueError, TP2_EJ4.perCirculo, -1)
        self.assertRaises(ValueError, TP2_EJ4.perCirculo, -10)

    def test_valoresAC(self):
        self.assertRaises(ValueError, TP2_EJ4.areaCirculo, -5)
        self.assertRaises(ValueError, TP2_EJ4.areaCirculo, -1)
        self.assertRaises(ValueError, TP2_EJ4.areaCirculo, -10)
if __name__ == "__main__":
    unittest.main()
