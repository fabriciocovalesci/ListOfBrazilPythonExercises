"""
3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

3. Make a program that checks if a typed letter is "F" or "M". 
As the letter writes: F - Female, M - Male, Invalid Gender.

"""

def masc_or_femin():
    enter = input('Type F - Female or M - Male: ')
    if enter in 'fF':
        print('\nYou reported - Female')
    elif enter in 'mM':
        print('\nYou reported - Male')
    else:
        print('\nInvalid Gender')

masc_or_femin()