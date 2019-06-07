import EJ4
import unittest


class testEJ4(unittest.TestCase):
    def test_capitalize(self):
        self.assertEqual(EJ4.capitalize("bitbucket", "bitbucket"), False)
        self.assertEqual(EJ4.capitalize("bitbucket", "Bitbucket"), True)

    def test_types(self):
        self.assertRaises(TypeError, EJ4.capitalize, 5, 6)
        self.assertRaises(TypeError, EJ4.capitalize, 5.5, 5.5)
        self.assertRaises(TypeError, EJ4.capitalize, True, False)
        self.assertRaises(TypeError, EJ4.capitalize, 5j + 1, 5j + 1)
if __name__ == "__main__":
    unittest.main()
