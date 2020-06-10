"""
[PT]
5. Altere o programa anterior permitindo ao usuário informar as populações e as taxas de 
crescimento iniciais. Valide a entrada e permita repetir a operação.

[EN]
5. Change the previous program allowing the user to inform populations and rates of
initial growth. Validate the entry and allow the operation to be repeated.
"""

validacao = True

while validacao:
    populacao_A = int(input("População A: "))
    populacao_B = int(input("População B: "))
    anos = int(input("Anos: ")
    if populacao_A or populacao_B > 0 and anos > 0:
        validacao = False
    else:
        print('População ou ano não pode ser menor que zero !!')


cres_A, cres_B = 0.03, 0.015 # Crescimentos de 3% e 1,5% ao ano
while (populacao_A < populacao_B):
    anos += 1
    populacao_A = populacao_A + (populacao_A * cres_A)
    populacao_B = populacao_B + (populacao_B * cres_B)
print("Após %i anos o país A ultrapassou o país B em número de habitantes." % anos)
print("País A: %.0f" % populacao_A)
print("País B: %.0f" % populacao_B)