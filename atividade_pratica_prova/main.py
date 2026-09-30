from ListaDuplamenteEncadeada import Lista

lista = Lista()

def menu_cadastro():

    print("""
=================================
    Histórico de navegador
=================================

1 - Acessar nova página
2 - Avançar página
3 - Voltar página
4 - Mostrar página atual
5 - Imprimir histórico
0 - Sair

=================================
""")

    return int(input("Digite uma opção: "))

opcao = -1

while opcao != 0:

    opcao = menu_cadastro()

    if opcao == 1:
        url = input("Digite a url: ")
        data_acesso = input("Digite a data de acesso: ")
        lista.acessarPag(url, data_acesso)

    elif opcao == 2:
        lista.avancar()

    elif opcao == 3:
        lista.voltar()

    elif opcao == 4:
        lista.pagAtual()

    elif opcao == 5:
        lista.historico()

    elif opcao == 0:
        print("Encerrando...")

    else:
        print("Opção inválida!")