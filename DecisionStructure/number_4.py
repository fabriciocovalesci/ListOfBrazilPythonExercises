"""
[PT]
4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

[EN]
4. Make a Program that checks if a typed letter is a vowel or consonant.
"""

def check_vowel_or_consonant():
    letter = input('Type a letter: ')
    if letter in 'aeiouAEIOU':
        print(f'\n{letter} -> typed letter is a vowel')
    else:
        print(f'\n{letter} -> letter is a consonant')

check_vowel_or_consonant()