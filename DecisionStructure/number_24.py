"""
[PT]
24. Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
    par ou ímpar;
    positivo ou negativo;
    inteiro ou decimal.

[EN]
24. Make a program that reads 2 numbers and then ask the user which operation he wants to perform.
The result of the operation must be accompanied by a sentence that says whether the number is:
    even or odd;
    positive or negative;
    integer or decimal.
"""

numero_1 = int(input('Digite um numero: '))
numero_2 = int(input('Digite outro numero: '))

print('\nQual operção deseja realizar? ')
op = int(input("""
\n1 - Adição
\n2 - Subtração
\n3 - Multiplicação
\n4 - Divisão
"""))

if op == 1:
    res = numero_1 + numero_2
    if res < 0:
        print(f"Numero {res} negativo")
    else:
        print(f'Numero {res} é positivo')
elif op == 2:
    res = numero_1 - numero_2
elif op == 3:
    res = numero_1 * numero_2
elif op == 4:
    res = numero_1 / numero_2
    