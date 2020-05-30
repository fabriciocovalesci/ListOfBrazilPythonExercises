"""
[PT]
12. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os 
descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e
3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado 
(é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, 
    dispostas conforme o exemplo abaixo.
    ** No exemplo o valor da hora é 5 e a quantidade de hora é 220.

    Salário Bruto: (5 * 220)        : R$ 1100,00
    (-) IR (5%)                     : R$   55,00  
    (-) INSS ( 10%)                 : R$  110,00
    FGTS (11%)                      : R$  121,00
    Total de descontos              : R$  165,00
    Salário Liquido                 : R$  935,00

[EN]
12. Make a program for the calculation of a payroll, knowing that the
The discounts are based on Income Tax, which depends on the gross salary (as shown in the table below) and
3% for the Union and that the FGTS corresponds to 11% of the Gross Salary, but is not discounted
(it is the company that deposits). The Net Salary corresponds to the Gross Salary less discounts.
The program should ask the user for the value of their hour and the number of hours worked in the month.
    IR discount:
    Gross salary up to 900 (inclusive) - exempt
    Gross Salary up to 1500 (inclusive) - 5% discount
    Gross Salary up to 2500 (inclusive) - 10% discount
    Gross Salary above 2500 - 20% discount Print the information on the screen,
    arranged according to the example below. In the example the hour value is 5 and the hour amount is 220.

"""

def calc_salary():
    valor_hora = float(input('Valor da hora: '))
    qtde_hora_mes = float(input('Quantidade de horas trabalhadas no mês: '))

    salario_bruto = valor_hora * qtde_hora_mes
    fgts = salario_bruto * 0.11
    sindicato = salario_bruto + (salario_bruto * 0.03)
    inss = salario_bruto * 0.10
    total_descontos = salario_bruto - (salario_bruto - inss)
    salario_liquido_isento = salario_bruto - total_descontos
    salario_liquido_ir_05 = salario_bruto - total_descontos - (salario_bruto * 0.05)
    salario_liquido_ir_10 = salario_bruto - total_descontos - (salario_bruto * 0.10)
    salario_liquido_ir_20 = salario_bruto - total_descontos - (salario_bruto * 0.20)
    
    if salario_bruto <= 900:
        print(f"""
            Salário Bruto:        : R$ {salario_bruto:.2f}
            (-) IR (0%)           : -- Isento  
            (-) INSS ( 10%)       : R$  {inss:.2f}
            FGTS (11%)            : R$  {fgts:.2f}
            Total de descontos    : R$  {abs(total_descontos):.2f}
            Salário Liquido       : R$  {salario_liquido_isento:.2f}
        """)
    elif salario_bruto > 900 and salario_bruto <= 1500:
            print(f"""
            Salário Bruto:        : R$ {salario_bruto:.2f}
            (-) IR (5%)           : R$ {(salario_bruto * 0.05):.2f}  
            (-) INSS ( 10%)       : R$ {inss:.2f}
            FGTS (11%)            : R$ {fgts:.2f}
            Total de descontos    : R$ {abs(total_descontos):.2f}
            Salário Liquido       : R$ {salario_liquido_ir_05:.2f}
        """)
    elif salario_bruto > 1500 and salario_bruto <= 2500:
            print(f"""
            Salário Bruto:        : R$ {salario_bruto:.2f}
            (-) IR (10%)          : R$ {(salario_bruto * 0.10):.2f}  
            (-) INSS ( 10%)       : R$ {inss:.2f}
            FGTS (11%)            : R$ {fgts:.2f}
            Total de descontos    : R$ {abs(total_descontos):.2f}
            Salário Liquido       : R$ {salario_liquido_ir_10:.2f}
        """)
    elif salario_bruto > 2500:
            print(f"""
            Salário Bruto:        : R$ {salario_bruto:.2f}
            (-) IR (20%)          : R$ {(salario_bruto * 0.20):.2f}  
            (-) INSS (10%)        : R$ {inss:.2f}
            FGTS (11%)            : R$ {fgts:.2f}
            Total de descontos    : R$ {abs(total_descontos):.2f}
            Salário Liquido       : R$ {salario_liquido_ir_20:.2f}
        """)


calc_salary()

