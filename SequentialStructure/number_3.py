"""
[PT]
3. Faça um Programa que peça dois números e imprima a soma.

[EN]
3. Make a Program that asks for two numbers and prints the sum.
"""


def sumtwonumber(n1: int, n2: int):
    n1 = int(input('\nEnter a number for n1: '))
    n1 = int(input('\nEnter a number for n2: '))
    sum_numbers = n1 + n1
    return f'\nSum of numbers n1 and n2 is: {sum_numbers}'