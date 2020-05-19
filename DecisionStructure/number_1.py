"""
[PT]
1. Faça um Programa que peça dois números e imprima o maior deles.

[EN]
1. Make a Program that asks for two numbers and prints the largest one.
"""


def greater_than_two_numbers():
    number1 = int(input("\nEnter a number for n1: "))

    number2 = int(input("\nEnter a number for n2: "))

    if number1 > number2:
        print(f"\nThe largest is number1 -> {number1}")
    else:
        print(f"\nThe largest is number2 -> {number2}")


greater_than_two_numbers()