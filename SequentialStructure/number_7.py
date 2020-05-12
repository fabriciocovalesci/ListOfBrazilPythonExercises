"""
[PT]
7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

[EN]
7. Make a program that calculates the area of ​​a square, then show twice the area to the user.
"""

def calc_square() -> float:
    side = float(input("\nSquare side size: "))
    print( f"{(side*side)*2}")


calc_square()