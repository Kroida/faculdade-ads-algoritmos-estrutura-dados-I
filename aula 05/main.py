from Carro import Carro
from Fila import Fila

fila = Fila()

def menu():
    print( " ------------------------------")
    print( "| 1) Adicionar carro na fila   |")
    print( "| 2) Lavar Carro               |")
    print( "| 3) Imprimir Fila             |")
    print( "| 4) Consultar posição na fila |")
    print( "| 5) Sair                      |")
    print( " ------------------------------")
    return int( input( "Digite a opção desejada: ") )

op = 0
while op != 5:
    op = menu()
    if op == 1:
        modelo = input("Qual modelo do carro: ")
        placa = input("Qual placa do carro: ")
        fila.add( Carro( placa, modelo)  )
    elif op == 2:
        fila.remover()
    elif op == 3: 
        fila.imprimir()
    elif op == 4:
        fila.getPosicao( input("Digite a placa que deseja consultar: ") )
    elif op == 5:
        print("Bye-bye!!!")
    else: 
        print("Opção inválida")