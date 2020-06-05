"""
[PT]
25. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?" 
    O programa deve no final emitir uma classificação sobre a 
    participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve 
    ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
    Caso contrário, ele será classificado como "Inocente".

[EN]
25. Make a program that asks a person 5 questions about a crime. The questions are:
    "Did you call the victim?"
    "Were you at the crime scene?"
    "Do you live near the victim?"
    "Should it be for the victim?"
    "Have you worked with the victim?" The program should at the end issue a rating on the
    person's participation in the crime. If the person answers positively to 2 questions he must
    be classified as "Suspect", between 3 and 4 as "Accomplice" and 5 as "Assassin".
    Otherwise, he will be classified as "Innocent".
"""

telefone = input('Telefonou para a vítima? (Sim - Não): ')
local = input('Esteve no local do crime? (Sim - Não): ')
mora = input("Mora perto da vítima? (Sim - Não): ")
divida = input("Devia para a vítima? (Sim - Não): ")
trabalho = input("Já trabalhou com a vítima? (Sim - Não): ")