"""
[PT]
9. Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a 
temperatura em graus Celsius. Fórmula matemática: C = (5 * (F-32) / 9).

[EN]
9. Make a Program that asks for the temperature in Farenheit degrees, transform and show the
temperature in degrees Celsius. Mathematical formula: C = (5 * (F-32) / 9).
"""

def calc_temperature_F_C():
    temp_Fare = int(input("The temperature in Farenheit degrees: "))
    print(f"Temperature in degrees Celsius: {(5 * (temp_Fare-32) / 9):.2f}°")

