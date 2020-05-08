from unittest import TestCase, main
from number_2 import enternumber


class TesteNumber1(TestCase):
    def test_enter_number(self):
        enter = 3
        self.assertEqual(enternumber(enter), 3)


main()