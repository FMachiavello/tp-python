import EJ4
import unittest


class testEJ4(unittest.TestCase):
<<<<<<< HEAD
    def test_pitagoras(self):
        self.assertEqual(EJ4.pitagoras(4, 1, 4, 5, 4, 5), )
        self.assertEqual(EJ4.pitagoras(8), 36)
        self.assertEqual(EJ4.pitagoras(10), 55)
        self.assertEqual(EJ4.pitagoras(1), 1)
=======
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

>>>>>>> b82af1983a3b74358863fe88ab4b77db971b7afa
if __name__ == "__main__":
    unittest.main()
