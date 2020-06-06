"""
[PT]
2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
mostrando uma mensagem de erro e voltando a pedir as informações.

[EN]
2. Make a program that reads a username and password and does not accept the same password as the username,
showing an error message and asking for information again.
"""

login = 'Fabricio'
senha = '1234'

while True:
    login_e = input('\nUsuário: ')
    senha_e = input("\nSenha: ")
    if  login_e == login and senha_e == senha:
        print(f'Seja bem vindo {login_e}\nAcesso autorizado')
        break
    else:
        print('\nLogin ou senha incorreto')