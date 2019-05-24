import TP2_EJ3
import unittest


class testTP2EJ3(unittest.TestCase):
    def test_areaRec(self):
        self.assertEqual(TP2_EJ3.areaRec(5, 4, 2, 1), 4.0)
        self.assertEqual(TP2_EJ3.areaRec(99, 44, 33, 22), 4235.0)
        self.assertEqual(TP2_EJ3.areaRec(998, 444, 335, 225), 428242.0)

    def test_type(self):
        self.assertRaises(TypeError, TP2_EJ3.areaRec, a=['a', 'b'],
                          b=['a', 'b'], c=['a', 'b'], d=['a', 'b'])
        self.assertRaises(TypeError, TP2_EJ3.areaRec, a=[True, True],
                          b=[False, False], c=[False, False], d=[False, False])
        self.assertRaises(TypeError, TP2_EJ3.areaRec, a=[1 + 5j, 1 + 5j],
                          b=[1 + 5j, 1 + 5j], c=[1 + 5j, 1 + 5j],
                          d=[1 + 5j, 1 + 5j])
if __name__ == "__main__":
    unittest.main()
