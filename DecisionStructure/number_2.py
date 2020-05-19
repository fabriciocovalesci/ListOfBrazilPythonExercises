"""
[PT]
2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

[EN]
2. Make a Program that asks for a value and shows on the screen whether the value is 
positive or negative.

"""

def number_is_positive_or_negative():
    number = int(input("\nEnter a number: "))
    if number < 0:
        print(f"\nNumber {number} is negative")
    else:
        print(f"\nNumber {number} is positive")