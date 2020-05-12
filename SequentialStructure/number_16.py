"""
[PT]
16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros 
quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros 
quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a 
quantidades de latas de tinta a serem compradas e o preço total.


[EN]
16. Make a program for a paint store. The program should ask for the size in meters
squares of the area to be painted. Consider that the ink coverage is 1 liter for every 3 meters
squares and that the paint is sold in 18-liter cans, which cost R $ 80.00. Inform the user to
quantities of paint cans to be purchased and the total price.
"""

def calc_paint_store(area: float):
    if area <= 54:
        print(f'Number of cans: one of 18 liter\nTotal price: R$ 80.00')
    else:
        cans = (area / 54) + 1
        price = cans * 80
        print(f"Number of cans: {cans:.2f}\nTotal price R$ {price:.2f}")



calc_paint_store(53)