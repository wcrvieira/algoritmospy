"""
# Menu de operações
# Autor: Wagner Cesar Vieira
# Data: 05/09/2022
# Hora: 17:10
"""

def somar(x, y):
    soma = x + y    
    return soma

def subtrair(x, y):
    sub = x - y    
    return sub

def dividir(x, y):
    div = x / y    
    return div

def multiplicar(x, y):
    mult = x * y    
    return mult

while True:
    print("""

Menu
----
1 - Adição
2 - Subtração
3 - Divisão
4 - Multiplicação
5 - Sair

""")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 5:
        break
    elif opcao >= 1 and opcao <=5:
        num1 = int(input("Digite o 1º valor: "))
        num2 = int(input("Entre com o 2º valor: "))

    if opcao == 1:
        soma = somar(num1, num2)
        print(f"\nA soma é {soma}")
        
    elif opcao == 2:
        sub = subtrair(num1,num2)
        print(f"\nA subtração é {sub}")
        
    elif opcao == 3:
        div = dividir(num1,num2)
        print(f"\nA divisão é {div:.2}")
        
    elif opcao == 4:
       mult = multiplicar(num1,num2)
       print(f"\nA multiplicação é {mult}")
        
    else:
        print("Opção inválida!")
