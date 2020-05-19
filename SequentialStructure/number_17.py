"""
[PT]
17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros 
quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 
6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 
ou em galões de 3,6 litros, que custam R$ 25,00.

    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos 
    preços em 3 situações:
    17.1: comprar apenas latas de 18 litros;
    17.2: comprar apenas galões de 3,6 litros;
    17.3: misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e 
    sempre arredonde os valores para cima, isto é, considere latas cheias.

[EN]
17. Make a program for a paint store. The program should ask for the size in meters
squares of the area to be painted. Consider that the ink coverage is 1 liter for each
6 square meters and that the paint is sold in 18-liter cans, which cost R $ 80.00
or in 3.6 liter gallons, which cost R $ 25.00.

    Inform the user of the quantities of ink to be purchased and the respective
    prices in 3 situations:
    17.1: buy only 18 liter cans;
    17.2: buy only 3.6 liters gallons;
    17.3: mix cans and gallons, so that the price is the lowest. Add 10% clearance and
    always round the values ​​up, that is, consider full cans.
"""

def calc_paint_store_part2(area: float):
    if area <= 54:
        print(f'Number of cans: one of 18 liter\nTotal price: R$ 80.00')
        print('\nOr:')
        gallons = (area / 21.6) + 1
        price_gallons = gallons * 25.00
        print(f'Number of gallons: {gallons:.2f} of 3.6 liter gallons\nTotal price: R$ {price_gallons:.2f}')

        if (price_gallons < 80.00):
            print(f'\nAdvantage to buy in 3.6 liter gallons\nPrice: R$ {price_gallons:.2f}')
        else:
            print(f'\nAdvantage to buy in 18 liter cans\nPrice: R$ 80.00')

    else:
        cans = (area / 54) + 1
        price = cans * 80
        print(f"Number of cans: {cans:.2f}\nTotal price R$ {price:.2f}")
        print('Or: ->')
        gallons = (area / 21.6) + 1
        price_gallons = gallons * 25.00
        print(f'Number of gallons: {gallons} of 3.6 liter gallons\nTotal price: R$ {price_gallons:.2f}')

        if (gallons > price):
            print(f'\nAdvantage to buy in 18 liter cans\nPrice: {price:.2f}')

calc_paint_store_part2(53)