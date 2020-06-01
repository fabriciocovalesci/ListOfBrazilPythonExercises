"""
[PT]
17. Faça um Programa que peça um número correspondente a um determinado ano e em seguida 
informe se este ano é ou não bissexto.

Condição 1: Ser múltiplo de 4 e não ser múltiplo de 100
Condição 2: Ser múltiplo de 400 (se for múltiplo de 400 automaticamente é de 4)

[EN]
17. Make a Program that asks for a number corresponding to a certain year and then
inform whether this year is leap or not.
"""

print('\n\tVerifica ano bisexto\n')
ano = int(input('Digite um ano(yyyy): '))

if (ano%4==0 and ano%100!=0) or (ano%400==0):
    print(f'{ano} é Bissexto')
else:
    print(f'{ano} Não é bissexto')