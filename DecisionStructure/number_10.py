"""
[PT]
10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino 
ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

[EN]
10. Make a program that asks what time you study. Ask to type M-morning or V-Evening or N-Night. 
Print the message "Good morning!", "Good afternoon!" or good night!" or "Invalid Value!", as appropriate.
"""

turno = input("\nQue turno voce estuda?\n1 - M-matutino\n2 - V-Vespertino\n3 - N- Noturno\n>> ")

if turno == '1':
    print('\nBom Dia!')
if turno == '2':
    print('\nBoa Tarde!')
if turno =='3':
    print('\nBoa Noite!')
else:
    print("\nValor Inválido!")