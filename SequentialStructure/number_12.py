"""
[PT]
12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule 
seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

[EN]
12. Taking as input data the height of a person, build an algorithm that calculates
your ideal weight, using the following formula: (72.7 * height) - 58
"""

def calc_weight(height: float):
    print(f"Your ideal weight is {(72.7 * height) - 58:.2f}") 


calc_weight(1.75)