"""
[PT]
15. A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
Faça um programa capaz de gerar a série até o n−ésimo termo.

[EN]
The Fibonacci series is formed by the sequence 1,1,2,3,5,8,13,21,34,55, ... 
Make a program capable of generating the series up to the nth term.
"""

numero = int(input("Que termo deseja encontrar: "))
ultimo=1
penultimo=1


if (numero==1) or (numero==2):
    print("1")
else:
    count=3
    while count <= numero:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
    print(termo)    