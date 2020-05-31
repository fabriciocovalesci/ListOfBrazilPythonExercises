"""
[PT]
15. Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os 
valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: 
equilátero, isósceles ou escaleno.
    Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;

[EN]
15. Make a Program that asks for the 3 sides of a triangle. The program should inform whether
values ​​can be a triangle. Indicate, if the sides form a triangle, if it is:
equilateral, isosceles or scalene.
    Tips:
    Three sides form a triangle when the sum of any two sides is greater than the third;
    Equilateral Triangle: three equal sides;
    Isosceles Triangle: any two equal sides;
    Scalene Triangle: three different sides;
"""

lado_1 = int(input("Lado 1: "))
lado_2 = int(input("Lado 2: "))
lado_3 = int(input("Lado 3: "))

if lado_1 + lado_2 > lado_3:
    if lado_1 == lado_2 and lado_1 == lado_3:
        print('Triângulo Equilátero')
    elif lado_1 == lado_2 or lado_2 == lado_3 or lado_1 == lado_3:
        print('Triângulo Isósceles')
    elif lado_1 != lado_2 and lado_3 or lado_2 != lado_1 and lado_3 or lado_1 != lado_3:
        print('Triângulo Escaleno')

else:
    print ('É impossivel ser um triângulo')