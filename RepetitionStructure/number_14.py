"""
[PT]
14. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números 
pares e a quantidade de números impares.

[EN]
14. Make a program that asks for 10 whole numbers, calculate and show the number of numbers
pairs and the number of odd numbers.
"""

numbers = []

for numero in range(10):
    n = int(input(f"Numero {numero+1}: "))
    numbers.append(n)

pares = 0
impar = 0

for n in numbers:
    if n % 2 == 0:
        pares += 1
    else:
        impar += 1

print(f"Total de pares: {pares}")
print(f'Total de impares: {impar}')
    
