import EJ7
import unittest


class testEJ7(unittest.TestCase):
    def test_Agendados(self):
        self.assertRaises(KeyError, EJ7.agenda("tito"), 1137569120)
        self.assertRaises(KeyError, EJ7.agenda("pepe"), 1136485968)
        self.assertRaises(KeyError, EJ7.agenda("luis"), 1187954231)

    def noAgendados(self):
        self.assertRaises(TypeError, EJ7.agenda("pedro"))
        self.assertRaises(TypeError, EJ7.agenda("Roberto"))
        self.assertRaises(TypeError, EJ7.agenda("Carlos"))
        self.assertRaises(TypeError, EJ7.agenda("Pepe32"))

    def test_valores(self):
        with self.assertRaises(ValueError):
            EJ7.agenda('')

if __name__ == "__main__":
    unittest.main()
