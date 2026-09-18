from Livro import Livro
from Pilha import Pilha

pilha = Pilha()

def menu():
    print( "---------------------------------")
    print( "| 1) Adicionar livro na pilha   |")
    print( "| 2) Remover livro da pilha     |")
    print( "| 3) Imprimir pilha de livros   |")
    print( "| 4) Posição de um livro        |")
    print( "| 0) Sair                       |")
    print( "---------------------------------")
    return int( input( "Digite a opção desejada: ") )

op = -1
while op != 0:
    op = menu()
    if op == 1:
        titulo = input("Qual o titulo do livro: ")
        autor = input("Quem é o autor do livro: ")
        pilha.add(titulo, autor)
    elif op == 2:
        resposta = input("Qual livro deseja remover?")
        pilha.remover(resposta)
    elif op == 3: 
        pilha.imprimir()
    elif op == 4:
        pilha.getPosicao( input("Digite a placa que deseja consultar: ") )
    elif op == 0:
        print("Bye-bye!!!")
    else: 
        print("Opção inválida")