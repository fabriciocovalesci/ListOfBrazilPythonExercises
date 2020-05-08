from unittest import TestCase, main
from number_1 import helloworld
from number_2 import enternumber
from number_3 import sumtwonumber


class TesteSequentialStructure(TestCase):

    def test_number_1(self):
        enter = "fabricio"
        expected = "\nfabricio Hello World"
        self.assertEqual(helloworld(enter), expected)


    def test_number_2(self):
        enter = 3
        expected = f'\nThe number entered was {enter}'
        self.assertEqual(sumtwonumber(), expected)


    def test_number_3(self):


main()