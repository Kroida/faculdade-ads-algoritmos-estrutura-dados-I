from Arvore import Arvore
from Carro import Carro

def menu():
    print( "\n ------------------------------")
    print( "| 1) Adicionar Valor           |")
    print( "| 2) Imprimir Em Ordem (ERD)   |")
    print( "| 3) Imprimir Pré-Ordem (RED)  |")
    print( "| 4) Imprimir Pós-Ordem (EDR)  |")
    print( "| 5) Imprimir Reverso (DRE)    |")
    print( "| 6) Imprimir em Nível         |")
    print( "| 0) Sair                      |")
    print( " ------------------------------")
    return int( input( "Digite a opção desejada: ") )

op = -1
arvore = Arvore()
while op != 0:
    op = menu()
    if op == 1:
        car = Carro()
        arvore.add( arvore.raiz , car )
    elif op == 2:
        if arvore.raiz is None:
            print("Árvore vazia!")
        else: 
            arvore.imprimir_em_ordem( arvore.raiz )
    elif op == 3:
        arvore.imprimir_pre_ordem( arvore.raiz ) if arvore.raiz else print("Árvore vazia!")
    elif op == 4:
            imprimir_pos_ordem( arvore.raiz ) if arvore.raiz else print("Árvore vazia!")
    elif op == 5:
            arvore.imprimir_reverso( arvore.raiz ) if arvore.raiz else print("Árvore vazia!")
    elif op == 6:
        arvore.imprimir_em_nivel(arvore.raiz) if arvore.raiz else print("Árvore vazia!")
    elif op == 0:
        print("Bye-Bye!!!")
    else:
        print("Opção inválida")