from unittest import TestCase
import main


class TestMain(TestCase):
    def test_diffie_hellman(self):
        self.assertEqual(main.diffie_hellman(1, 2, 3, 4), 1)
        self.assertEqual(main.diffie_hellman(5, 10, 15, 20), 5)
        self.assertEqual(main.diffie_hellman(145, 264, 354, 564), 252)


