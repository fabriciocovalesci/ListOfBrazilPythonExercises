"""
[PT]
17. Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
Ex.: 5!=5.4.3.2.1=120

[EN]
17. Make a program that calculates the factorial of an integer provided by the user.
Ex .: 5! = 5.4.3.2.1 = 120
"""

number = int(input("Informe um número: "))
count_1 = 0
count = 1
while count_1 <= number:
    fatorial = number * (number - count)
    count = count - 1
    count_1 = count + 1

print(fatorial)

