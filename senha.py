"""
# Validador de senhas
# Autor: Wagner Cesar Vieira
# Data: 05/09/2022
# Hora: 16:30456
"""


def Verifica(senha):
    senhaCorreta = 'Senha123@'
    while senha != senhaCorreta:
        print('Senha incorreta!')
        senha = input('Digite novamente: ')
    else:
        print('Você está logado!')


Verifica(senha = input('Olá, informe sua senha: '))
