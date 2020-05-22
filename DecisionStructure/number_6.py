"""
[PT]
6. Faça um Programa que leia três números e mostre o maior deles.

[EN]
6. Make a Program that reads three numbers and shows the biggest one.
"""

def reads_three_numbers():
    numbers_1 = int(input('\nNumber I: '))
    numbers_2 = int(input('\nNumber II: '))
    numbers_3 = int(input('\nNumber III: '))

    if numbers_1 > numbers_2 and numbers_1 > numbers_3:
        print(f'\nNumber I {numbers_1} is bigger')
    elif numbers_2 > numbers_1 and numbers_2 > numbers_3:
        print(f'\nNumber II {numbers_2} is bigger')
    elif numbers_3 > numbers_1 and numbers_3 > numbers_2:
        print(f'\nNumber III {numbers_3} is bigger')

reads_three_numbers()