from unittest import TestCase, main
from number_1 import helloworld


class TesteNumber1(TestCase):
    def test_hello_world(self):
        enter = "fabricio"
        expected = "\nfabricio Hello World"
        self.assertEqual(helloworld(enter), expected)


main()