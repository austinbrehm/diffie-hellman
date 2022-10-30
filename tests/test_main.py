from unittest import TestCase
import main


class TestMain(TestCase):
    def test_diffie_hellman(self):
        result = main.diffie_hellman(5, 10, 15, 20)
        self.assertEqual(result, 5)

