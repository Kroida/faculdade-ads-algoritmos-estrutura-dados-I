from Arvore import Arvore

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
        valor = input("Digite o valor que será inserido: ")
        arvore.add( arvore.raiz , valor )
    elif op == 2:
        if arvore.raiz is None:
            print("Árvore vazia!")
        else: 
            arvore.imprimirEmOrdem( arvore.raiz )
    elif op == 3:
        arvore.imprimirPreOrdem( arvore.raiz ) if arvore.raiz else print("Árvore vazia!")
    elif op == 4:
            arvore.imprimirPosOrdem( arvore.raiz ) if arvore.raiz else print("Árvore vazia!")
    elif op == 5:
            arvore.imprimirReverso( arvore.raiz ) if arvore.raiz else print("Árvore vazia!")
    elif op == 6:
        arvore.imprimirEmNível(arvore.raiz) if arvore.raiz else print("Árvore vazia!")
    elif op == 0:
        print("Bye-Bye!!!")
    else:
        print("Opção inválida")
