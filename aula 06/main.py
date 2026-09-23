from Livro import Livro
from Pilha import Pilha

pilha = Pilha()

def menu():
    print("""
    ---------------------------------
    | 1) Adicionar livro na pilha   |
    | 2) Remover o primeiro livro   |
    |    da pilha                   |
    | 3) Imprimir pilha de livros   |
    | 4) Posição de um livro        |
    | 5) Posição de um livro pelo   |
    |    autor                      |
    | 0) Sair                       |
    ---------------------------------
    """)
    return int( input( "Digite a opção desejada: ") )

op = -1
while op != 0:
    op = menu()
    if op == 1:
        titulo = input("Qual o titulo do livro? ")
        autor = input("Quem é o autor do livro? ")
        qtdPag = input("Quantas páginas possui? ")
        pilha.add(titulo, autor, qtdPag)
    elif op == 2:
        pilha.remover()
    elif op == 3: 
        pilha.imprimir()
    elif op == 4:
        pilha.getPosicao( input("Digite o livro que deseja consultar: ") )
    elif op == 5:
        pilha.getPosicaoAutor( input("Digite o autor que deseja consultar: ") )
    elif op == 0:
        print("Bye-bye!!!")
    else: 
        print("Opção inválida")