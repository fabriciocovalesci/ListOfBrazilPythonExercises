"""
[PT]
11. Altere o programa anterior para mostrar no final a soma dos números.

[EN]
11. Change the previous program to show the sum of the numbers at the end.
"""

import random

number_1 = int(input("Numero 1: "))
number_2 = int(input("Numero 2: "))

numero_aleatorio = random.randrange(number_1, number_2, 1)
soma_total = number_1 + number_2 + numero_aleatorio

print(f"Numero aleatório {numero_aleatorio}")
print(f"Soma de todos numeros {soma_total}")

