"""
[PT]
14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento 
diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo 
regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo 
excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e 
calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável 
multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.


[EN]
14. João Papo-de-Pescador, a good man, bought a microcomputer to control income
diary of your work. Every time he brings a fish weight greater than that established by the
fishing regulations of the state of São Paulo (50 kilos) must pay a fine of R $ 4.00 per kilo
surplus. João needs you to make a program that reads the variable weight (fish weight) and
calculate the excess. Record in the excess variable the amount of kilos beyond the limit and in the variable
fine the amount of the fine that João must pay. Print the program data with the appropriate messages.
"""

def papo_pescador(peso: float):
    if peso <= 50:
        print(f"No fines, weigth total is {peso}")
    else:
        excess_weight = abs(50 - peso) * 4
        print(f'Fine amount R$ {excess_weight:.2f}')

papo_pescador(50)