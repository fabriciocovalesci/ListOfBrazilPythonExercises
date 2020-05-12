"""
[PT]
8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.

[EN]
8. Make a Program that asks how much you earn per hour and the number of hours worked in the month. 
Calculate and show your total salary for that month.
"""

def calc_salary():
    value_hour = float(input("\nHourly value: "))
    hour_worked_month = int(input("\nNumber of hours worked in the month: "))
    total = value_hour * hour_worked_month
    print(f"Your total salary for that month US$ {total:.2f}")

calc_salary()