import EJ4
import unittest


class testEJ4(unittest.TestCase):
    def test_numerosIguales(self):
        self.assertEqual(EJ4.pitagoras(lx=[-1, 3, -7], ly=[4, 3, 1]), (-7, 1))
        self.assertEqual(EJ4.pitagoras(lx=[2, 3, 6], ly=[6, 3, 4]), (6, 4))
        self.assertEqual(EJ4.pitagoras(lx=[-5, 3, 1], ly=[-3, 1, 5]), (-5, -3))

    def test_types(self):
        self.assertRaises(TypeError, EJ4.pitagoras, lx=[True, False, True],
                          ly=[True, False, True])

    def test_valores(self):
        self.assertRaises(ValueError, EJ4.pitagoras, lx=['', '', ''],
                          ly=['', '', ''])

if __name__ == "__main__":
    unittest.main()
