"""
4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.

4. Make a Program that asks for the 4 bimonthly notes and shows the average.
"""

bimonthly = []

for note in range(4):
    note = int(input(f'Note {note+1}: '))
    bimonthly.append(note)

print(f'\nAverage {sum(bimonthly)/len(bimonthly)}')
