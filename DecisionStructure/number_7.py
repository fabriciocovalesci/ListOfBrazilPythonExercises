"""
[PT]
7. Faça um Programa que leia três números e mostre o maior e o menor deles.

[EN]
7. Make a Program that reads three numbers and shows the biggest and the smallest.
"""

def bigger_and_smaller_displays():
    numbers_1 = int(input('\nNumber I: '))
    numbers_2 = int(input('\nNumber II: '))
    numbers_3 = int(input('\nNumber III: '))

    biggest = numbers_1
    smallest = numbers_1

    if biggest < numbers_2:
        biggest = numbers_2

    if biggest < numbers_3: 
        biggest = numbers_3

    if smallest > numbers_2:
        smallest = numbers_2

    if smallest > numbers_3:
        smallest = numbers_3

    print (f'\nBiggest:  {biggest}')
    print (f'Smallest:  {smallest}')

bigger_and_smaller_displays()