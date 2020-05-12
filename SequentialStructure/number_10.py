"""
[PT]
10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.

[EN]
10. Make a Program that asks for the temperature in degrees Celsius, transform it and show it in degrees Farenheit.
"""

def calc_temperature_C_F():
    temp_celsius = float(input("Temperature in degrees Celsius: "))
    print(f"Temperature in Farenheit: {(temp_celsius * 1.8) + 32:.2f}")



calc_temperature_C_F()