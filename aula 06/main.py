from Livro import Livro
from Pilha import Pilha

pilha = Pilha()

def menu():
    print( "---------------------------------")
    print( "| 1) Adicionar livro na pilha   |")
    print( "| 2) Folear livro               |")
    print( "| 3) Imprimir pilha             |")
    print( "| 4) Consultar posição na pilha |")
    print( "| 0) Sair                       |")
    print( "---------------------------------")
    return int( input( "Digite a opção desejada: ") )

op = -1
while op != 0:
    op = menu()
    if op == 1:
        titulo = input("Qual o titulo do livro: ")
        autor = input("Quem é o autor do livro: ")
        pilha.add(Livro( autor, titulo))
    elif op == 2:
        pilha.remover()
    elif op == 3: 
        pilha.imprimir()
    elif op == 4:
        pilha.getPosicao( input("Digite a placa que deseja consultar: ") )
    elif op == 0:
        print("Bye-bye!!!")
    else: 
        print("Opção inválida")