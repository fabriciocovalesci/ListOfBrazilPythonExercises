"""
[PT]
8. Faça um programa que leia 5 números e informe a soma e a média dos números.

[EN]
8. Make a program that reads 5 numbers and gives the sum and average of the numbers.
"""

lista_notas = []

for nota in range(5):
    notas  = int(input("\nNota: "))
    lista_notas.append(notas)

soma_total = sum(lista_notas)
media = soma_total / len(lista_notas)

print(f"Soma dos numeros {soma_total}")
print(f"Media dos numeros informados {media:.2f}")
