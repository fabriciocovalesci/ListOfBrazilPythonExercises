"""
[PT]
4. Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de 
crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
Faça um programa que calcule e escreva o número de anos necessários para que a população do país 
A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

[EN]
4. Assuming that the population of country A is of the order of 80000 inhabitants with an annual rate of
growth of 3% and that the population of B is 200000 inhabitants with a growth rate of 1.5%.
Make a program that calculates and writes the number of years needed for the country's population
A exceeds or equals the population of country B, with growth rates maintained.
"""

populacao_A, populacao_B, anos = 80000, 200000, 0
cres_A, cres_B = 0.03, 0.015 # Crescimentos de 3% e 1,5% ao ano
while (populacao_A < populacao_B):
    anos += 1
    populacao_A = populacao_A + (populacao_A * cres_A)
    populacao_B = populacao_B + (populacao_B * cres_B)
print("Após %i anos o país A ultrapassou o país B em número de habitantes." % anos)
print("País A: %.0f" % populacao_A)
print("País B: %.0f" % populacao_B)