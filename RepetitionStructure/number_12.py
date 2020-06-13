"""
[PT]
12. Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. 
O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
    Tabuada de 5:
    5 X 1 = 5
    5 X 2 = 10
    ...
    5 X 10 = 50

[EN]
12. Develop a multiplication table generator, capable of generating the multiplication table for any integer between 1 to 10.
The user must inform which number he wants to see the multiplication table. The output should be according to the example below:
    Times table of 5:
    5 X 1 = 5
    5 X 2 = 10
    ...
    5 X 10 = 50
"""

tabuada = int(input("Qual tabuada deseja: "))

for numero in range(0, 10+1, 1):   
    resultado = tabuada * numero
    print(f"{tabuada} X {numero}  = {resultado}") 