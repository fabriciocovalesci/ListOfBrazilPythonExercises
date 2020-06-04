"""
[PT]
20. Faça um Programa para leitura de três notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e presentar:
    A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
    A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
    A mensagem "Aprovado com Distinção", se a média for igual a 10.

[EN]
20. Make a Program to read a student's three partial grades.
The program should calculate the average achieved per student and present:
    The message "Approved", if the average is greater than or equal to 7, with the respective average achieved;
    The message "Failed", if the average is less than 7, with the respective average achieved;
    The message "Approved with Distinction", if the average is equal to 10.
"""

nota_1 = int(input('Nota 1: '))
nota_2 = int(input('Nota 2: '))
nota_3 = int(input('Nota 3: '))

media = (nota_1 + nota_2 + nota_3) / 3

if media >= 7 and media < 9.9:
    print(f'{media:.2f}: Aprovado')
elif media < 7:
    print(f'{media:.2f}: Reprovado')
elif media == 10:
    print(f'{media:.2f}: Aprovado com Distinção')


