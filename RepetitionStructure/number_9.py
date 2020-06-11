"""
[PT]
9. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

[EN]
9. Make a program that prints on the screen only the odd numbers between 1 and 50.
"""

for numero in range(1,50+1):
    if numero % 2 != 0:
        print(numero)