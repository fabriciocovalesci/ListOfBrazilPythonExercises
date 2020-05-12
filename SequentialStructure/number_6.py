"""
[PT]
6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

[EN]
6. Make a Program that asks for the radius of a circle, calculate and show its area.
"""

def calc_area():
    pi = 3.141592
    enter_radius = int(input("\nRadius of a circle: "))
    print(f'Area of circle is {float(pi*(enter_radius**2)):.2f}')


calc_area()