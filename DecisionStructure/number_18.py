"""
[PT]
18. Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

[EN]
18. Make a Program that asks for a date in the format mm/dd/yyyy and determine if it is a valid date.
"""


data_valida = True

while data_valida:
    data = input('Informe data dd/mm/aaaa -> ')

    dia = int(data[0:2])
    mes = int(data[3:5])
    ano = int(data[6:])

    if dia >= 1 and dia <= 12 and mes >= 1 and mes <= 31 and ano > 0:
        data_valida = False
        print("Data Válida")
    else:
        print("\ndata invalida...\n")
        data_valida = True
        

