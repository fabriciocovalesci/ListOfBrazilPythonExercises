from unittest import TestCase, main
from number_1 import helloworld
from number_2 import enternumber
from number_3 import sumtwonumber


class TesteSequentialStructure(TestCase):

    def test_number_1(self):
        text = "Hello World"
        hello_world = helloworld(text)
        self.assertTrue(hello_world)


    def test_number_2(self):
        enter = 3
        expected = f'\nThe number entered was {enter}'
        self.assertEqual(enternumber(), expected)


    # def test_number_3(self):
main()