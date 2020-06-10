"""
[PT]
7. Faça um programa que leia 5 números e informe o maior número.

[EN]
7. Make a program that reads 5 numbers and reports the largest number.
"""

n_1 = int(input("Numero 1: ")) 
n_2 = int(input("Numero 2: ")) 
n_3 = int(input("Numero 3: ")) 
n_4 = int(input("Numero 4: ")) 
n_5 = int(input("Numero 5: "))

maior = [n_1, n_2, n_3, n_4, n_5]

for number in maior:
    n = number
    if number > n