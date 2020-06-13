"""
[PT]
13. Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado 
ao segundo número. 
Não utilize a função de potência da linguagem.

[EN]
13. Make a program that asks for two numbers, base and exponent, calculate and show the first number 
raised to the second number.
Do not use the language power function.
"""


print("Base | Expoente\n")
base = int(input("Base: "))
expoente = int(input("Expoente: "))

potencia = 1

for count in range(expoente):
    potencia *= base
    count += 1

print(f"{base} ^ {expoente} = {potencia}")