"""
[PT]
18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade 
de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo
usando este link (em minutos).

[EN]
18. Make a program that asks for the size of a file to download (in MB) and the speed of an 
Internet link (in Mbps), calculate and inform the approximate time to download the file using 
this link (in minutes).
"""

def calc_time_download():
    file = float (input("informe o tamanho do arquivo:"))
    speed = float (input("informe a velocidade de conexao:"))
    time = file / speed
    print ("A velocidade de download do arquivo e: " , time)

calc_time_download()