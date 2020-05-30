"""
[PT]
13. Faça um Programa que leia um número e exiba o dia correspondente da semana. 
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

[EN]
13. Make a Program that reads a number and displays the corresponding day of the week.
(1-Sunday, 2-Monday, etc.), if you enter another value, an invalid value should appear.
"""

def day_week(number: int):
    if number == 1:
        print("1-Sunday")
    elif number == 2:
        print('2-Monday')
    elif number == 3:
        print('3-Tuesday') 
    elif number == 4:
        print('4-Wednesday')
    elif number == 5:
        print('5-Thursday')
    elif number == 6:
        print('6-Friday')
    elif number == 7:
        print('7-Saturday')
    else:
        print('Invalid value!!')
    
day_week(8)