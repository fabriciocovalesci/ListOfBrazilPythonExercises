"""
[PT]
8. Faça um programa que pergunte o preço de três produtos e informe qual 
produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

[EN]
8. Make a program that asks the price of three products and tells you which 
product you should buy, knowing that the decision is always for the cheapest.
"""


def buy_cheaést():
    price_1 = float(input('\nPrice I: '))
    price_2 = float(input('\nPrice II: '))
    price_3 = float(input('\nPrice III: '))

    bigger_price = price_1
    smallest_price = price_1

    if smallest_price > price_2:
        smallest_price = price_2

    if smallest_price > price_3:
        smallest_price = price_3

    print(f'\nCheapest to buy is {smallest_price:.2f}')

buy_cheaést()