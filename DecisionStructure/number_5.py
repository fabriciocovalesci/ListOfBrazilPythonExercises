"""
[PT]
5. Faça um programa para a leitura de duas notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e apresentar:
    - A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    - A mensagem "Reprovado", se a média for menor do que sete;
    - A mensagem "Aprovado com Distinção", se a média for igual a dez.

[EN]
5. Make a program for reading a student's two partial grades. 
The program should calculate the average achieved per student and present:
    - The message "Approved", if the average reached is greater than or equal to seven;
    - The message "Failed", if the average is less than seven;
    - The message "Approved with distinction", if the average is equal to ten.

"""

def average_student():
    partial_1 = float(input("Partial 1 -> "))
    partial_2 = float(input('Partial 2 -> '))

    average = (partial_1 + partial_2) / 2

    if average >= 7.0 and average < 9.99:
        print(f'\nApproved\nAverage: {average}')
    elif average < 7.0:
        print(f'\nFailed\nAverage: {average}')
    elif average == 10:
        print(f'\nApproved with distinction\nAverage: {average}')

average_student()