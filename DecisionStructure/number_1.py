"""
1. Faça um Programa que peça dois números e imprima o maior deles.
1. Make a Program that asks for two numbers and prints the largest one.
"""

n1 = int(input("\nEnter a number for n1: "))

n2 = int(input("\nEnter a number for n2: "))

if n1 > n2:
    print(f"\nThe largest is n1 -> {n1}")
else:
    print(f"\nThe largest is n2 -> {n2}")