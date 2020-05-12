"""
[PT]
15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o 
Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

15.1: salário bruto.
15.2: quanto pagou ao INSS.
15:3 quanto pagou ao sindicato.
15.4: o salário líquido.

calcule os descontos e o salário líquido, conforme a tabela abaixo:
    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido.


[EN]
15. Make a Program that asks how much you earn per hour and the number of hours worked in the month.
Calculate and show the total of your salary in that month, knowing that 11% are discounted for the
Income Tax, 8% for the INSS and 5% for the union, make a program that gives us:

15.1: gross salary.
15.2: how much you paid INSS.
15: 3 how much you paid the union.
15.4: the net salary.

calculate the discounts and net salary, according to the table below:
    + Gross Salary: R $
    - IR (11%): R $
    - INSS (8%): ​​R $
    - Union (5%): R $
    = Net Salary: R $

Note: Gross Salary - Discounts = Net Salary.
"""


def calc_salary_total(hour: float, hour_worked: float):
    gross_salary = hour * hour_worked
    disc_ir = gross_salary * 0.11 
    disc_inss = gross_salary * 0.08
    disc_union = gross_salary * 0.05
    net_salary = abs(gross_salary - disc_ir - disc_inss -disc_union)
    print(f"""
    \n+ Gross Salary: R$ {gross_salary:.2f}
    \n- IR (11%): R$ {disc_ir:.2f}
    \n- INSS (8%): ​​R$ {disc_inss:.2f}
    \n- Union (5%): R$ {disc_union:.2f}
    \n= Net Salary: R$ {net_salary:.2f}
    """)


calc_salary_total(200, 12.5)