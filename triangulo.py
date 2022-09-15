"""
# Analisador de trinângulos
# Autor: Wagner Cesar Vieira
# Data: 05/09/2022
# Hora: 16:45
"""

print('-=-'*20)
print ('Analisador de triangulo')
print('-=-'*20)

a = float(input('Informe o valor do lado A: '))
b = float(input('Digite o valor do lado B: '))
c = float(input('Entre com o valor do lado C: '))

if a > (b+c) or b > (a+c) or c > (a+b):
    print ('Não é um triangulo')
elif (a==b) and (a==c):
    print('Equilatero')
elif (a==b) or (a==c) or (b==c):
    print('Isoceles ')
else:
    print('escaleno')
