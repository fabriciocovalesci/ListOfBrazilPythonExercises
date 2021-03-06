"""
[PT]
11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver 
o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

    - salários até R$ 280,00 (incluindo) : aumento de 20%
    - salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    - salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    - salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    - o salário antes do reajuste;
    - o percentual de aumento aplicado;
    - o valor do aumento;
    - o novo salário, após o aumento.

[EN]
11. Tabajara Organizations decided to give their employees a salary increase and hired them to develop the 
program that will calculate the adjustments.
Make a program that receives an employee's salary and readjust it according to the following criteria, 
based on the current salary:

    - wages up to R $ 280.00 (including): 20% increase
    - wages between R $ 280.00 and R $ 700.00: increase of 15%
    - wages between R $ 700.00 and R $ 1500.00: 10% increase
    - salaries from R $ 1500.00 onwards: increase of 5% After the increase is made, inform on the screen:
    - the salary before the readjustment;
    - the percentage of increase applied;
    - the amount of the increase;
    - the new salary after the increase.
"""

def calc_reajustes(salario_colaborador: float):
    reaj1 = 0.20
    reaj2 = 0.15
    reaj3 = 0.10
    reaj4 = 0.05
    salary = salario_colaborador

    if salary <= 280:
        reajuste_salario = salary + (salary * reaj1)
        print(f'\nSalario antes do reajuste R$ {salary}')
        print(f'Percentual de aumento aplicado {reaj1 * 100} %')
        print(f'O valor do aumento R$ {abs(salary - reajuste_salario):.2f}')
        print(f'Novo salario R$ {reajuste_salario:.2f}\n')

    elif salary > 280 and salary < 700:
        reajuste_salario = salary + (salary * reaj2)
        print(f'\nSalario antes do reajuste R$ {salary}')
        print(f'Percentual de aumento aplicado {reaj2 * 100} %')
        print(f'O valor do aumento R$ {abs(salary - reajuste_salario):.2f}')
        print(f'Novo salario R$ {reajuste_salario:.2f}\n')

    elif salary > 700 and salary < 1500:
        reajuste_salario = salary + (salary * reaj3)
        print(f'\nSalario antes do reajuste R$ {salary}')
        print(f'Percentual de aumento aplicado {reaj3 * 100} %')
        print(f'O valor do aumento R$ {abs(salary - reajuste_salario):.2f}')
        print(f'Novo salario R$ {reajuste_salario:.2f}\n')

    elif salary > 1500:
        reajuste_salario = salary + (salary * reaj4)
        print(f'\nSalario antes do reajuste R$ {salary}')
        print(f'Percentual de aumento aplicado {reaj4 * 100} %')
        print(f'O valor do aumento R$ {abs(salary - reajuste_salario):.2f}')
        print(f'Novo salario R$ {reajuste_salario:.2f}\n')


calc_reajustes(500)