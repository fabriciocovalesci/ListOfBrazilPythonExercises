"""
[PT]
11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    11.1: o produto do dobro do primeiro com metade do segundo .
    11.2: a soma do triplo do primeiro com o terceiro.
    11.3: o terceiro elevado ao cubo.

[EN]
11. Make a Program that asks for 2 whole numbers and a real number. Calculate and show:
    11.1: the product of double the first with half the second.
    11.2: the sum of triple the first with the third.
    11.3: the third raised to the cube.
"""

def calc_numbers(n1: int, n2: int, n3: float):
    case_1 = (n1*2) * (n2/2)
    case_2 = (n1*n1*n1) + n3
    case_3 = n3*3
    print(f"Case 1: {case_1}\nCase 2: {case_2}\nCase 3: {case_3}")

calc_numbers(2, 3, 4.0)