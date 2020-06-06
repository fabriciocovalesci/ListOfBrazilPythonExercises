"""
[PT]
1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja 
inválido e continue pedindo até que o usuário informe um valor válido.

[EN]
1. Make a program that asks for a note, between zero and ten. Show a message if the value is
invalid and keep asking until the user enters a valid value.
"""

while True:
    nota = int(input("\nInforme uma nota(0-10): "))
    if nota >= 0 and nota <= 10:
        print(f'\nNota digitada: {nota}')
        break
    else:
        print(f"\nInforme um valor válido 0-10")