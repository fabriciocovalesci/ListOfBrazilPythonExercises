"""
[PT]
2. Faça um Programa que peça um número e então mostre a mensagem "O número informado foi [número]".

[EN]
2. Make a Program that asks for a number and then displays the message "The number entered was [number]".
"""


def enternumber() -> str:
    number = input('\nEnter a number: ')
    return f'\nThe number entered was {number}'
