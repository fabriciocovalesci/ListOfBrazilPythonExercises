from unittest import TestCase, main
from number_1 import helloworld


class TesteNumber1(TestCase):
    def test_number(self):
        enter = "hi"
        expected = int
        self.assertEqual(helloworld(enter), expected)

