"""
[PT]
13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que 
calcule seu peso ideal, utilizando as seguintes fórmulas:
    13.1: Para homens: (72.7*h) - 58
    13.2: Para mulheres: (62.1*h) - 44.7

[EN]
13. Taking as input the height (h) of a person, build an algorithm that calculates 
your ideal weight, using the following formulas:
    13.1: For men: (72.7 * h) - 58
    13.2: For women: (62.1 * h) - 44.7
"""

def calc_ideal_weight(h: float):
    print(f'For men: {(72.7 * h) - 58:.2f}')
    print(f'For women: {(62.1 * h) - 44.7:.2f}')

calc_ideal_weight(1.75)