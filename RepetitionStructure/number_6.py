"""
[PT]
6. Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
Depois modifique o programa para que ele mostre os números um ao lado do outro.

[EN]
6.  Make a program that prints the numbers from 1 to 20, one below the other. 
Then modify the program so that it shows the numbers next to each other.
"""

for numero in range(20+1):
    print(f"Número: {numero}\n")

for numero in range(20+1):
    print(f"Número: {numero}",end=' ')