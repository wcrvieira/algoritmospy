"""
# Média e soma de valores
# Autor: Wagner Cesar Vieira
# Data: 05/09/2022
# Hora: 15:40
"""

def media(valores):
    media = sum(valores) / len(valores)
    print(f'A média é {media}')

def soma(numeros):
    soma = sum(numeros)
    print(f'A soma é {soma}')

lista = []

for i in range(5):
    lista.append(int(input('Entre com um valor: ')))
print(f'Valores da lista: {lista}')

media(lista)
soma(lista)

