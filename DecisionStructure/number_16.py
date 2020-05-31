"""
[PT]
16. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas 
seguintes situações:
    A. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o 
    programa não deve fazer pedir os demais valores, sendo encerrado;
    B. Se o delta calculado for negativo, a equação não possui raizes reais. 
    Informe ao usuário e encerre o programa;
    C. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    D. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

[EN]
16. Make a program that calculates the roots of a second degree equation, in the form ax2 + bx + c.
The program should ask for the values ​​of a, b and c and make the consistencies, informing the user in the
following situations:
    A. If the user inputs the value of A equal to zero, the equation is not of the second degree and the
    the program should not ask for the other values, being closed;
    B. If the calculated delta is negative, the equation has no real roots.
    Inform the user and close the program;
    C. If the calculated delta is equal to zero, the equation has only one real root; inform the user;
    D. If the delta is positive, the equation has two real roots; inform the user;
"""

import math


print('\tEquação do segundo grau\n')
a = int(input('Valor para A: '))
if a != 0:
    b = int(input('Valor para B: '))
    c = int(input('Valor para C: '))
    delta = (math.pow(b,2) - (4*a*c))

    if delta < 0:
        print('Delta menor que 0\n')
    elif delta == 0:
        raiz = -b / (2*a)
        print(f'Delta=0 , raiz = {raiz}')
    else:
        raiz1 = (-b + math.sqrt(delta) ) / (2*a)
        raiz2 = (-b - math.sqrt(delta) ) / (2*a)
        print(f'Raizes: {raiz1} e {raiz2}')
else:
    print("\nPrograma encerrado, valor de A deve ser diferente de 0\n")