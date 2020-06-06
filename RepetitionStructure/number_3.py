"""
[PT]
3. Faça um programa que leia e valide as seguintes informações:
    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd';

[EN]
3. Make a program that reads and validates the following information:
    Name: greater than 3 characters;
    Age: between 0 and 150;
    Salary: greater than zero;
    Gender: 'f' or 'm';
    Civil Status: 's', 'c', 'v', 'd';
"""

import string

nome = input('Nome: ')
idade = int(input('Idade: '))
salario: float(input('Salário: '))
sexo = input('Sexo (f-m): ')
est_civil = input('Estado civil(s-c-v-d): ')
print(len(nome))
if len(nome) > 3 and idade >= 0 or idade < 150 and  sexo in 'fmFM' and est_civil in 'scvdSCVD':
    print('passou')
else:
    print("Algum dado foi informado incorretamente !!")