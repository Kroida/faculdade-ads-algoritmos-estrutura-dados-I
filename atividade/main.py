from Fila import Fila
from ListaEncadeada import Lista
from Apartamento import Apartamento
from Torre import Torre
from Array import myArray


torre = Torre(1, "torreae", "1053-35")

lista = Lista()
fila = Fila()

# Array que representa as 5 vagas do condomínio
vagas = myArray(5)


def inicializar_vagas():
    for i in range(5):
        vagas.adicionar(i, None)


def encontrar_vaga():
    for i in range(5):
        if vagas.acessar(i) is None:
            return i + 1

    return None


def ocupar_vaga(numero_vaga, apartamento):
    indice = numero_vaga - 1
    vagas.adicionar(indice, apartamento)


def liberar_vaga(numero_vaga):
    indice = numero_vaga - 1
    return vagas.remover(indice)


def cadastrar_apartamento():

    print("\n--- Cadastro de apartamento ---")

    id_ap = int(input("Qual o ID do apartamento? "))
    numero = input("Qual o número do apartamento? ")

    vaga = encontrar_vaga()

    if vaga is not None:

        apartamento = Apartamento(
            id_ap,
            numero,
            torre,
            vaga
        )

        ocupar_vaga(vaga, apartamento)

        lista.adicionar(apartamento)

        print(
            f"✅ Apartamento {id_ap} "
            f"cadastrado na vaga {vaga}!"
        )

    else:

        apartamento = Apartamento(
            id_ap,
            numero,
            torre
        )

        fila.adicionar(apartamento)

        print(
            f"⏳ Não existem vagas disponíveis."
        )

        print(
            f"Apartamento {id_ap} "
            f"adicionado à fila de espera!"
        )


def liberar_vaga_apartamento():

    print("\n--- Liberar vaga ---")

    id_ap = int(
        input("Qual o ID do apartamento? ")
    )

    apartamento = lista.remover(id_ap)

    if apartamento is None:
        return

    vaga = apartamento.vaga

    liberar_vaga(vaga)

    print(
        f"🔓 Vaga {vaga} liberada!"
    )

    # Verifica se existe alguém esperando
    if fila.inicio is not None:

        proximo = fila.remover()

        proximo.vaga = vaga

        ocupar_vaga(vaga, proximo)

        lista.adicionar(proximo)

        print(
            f"✅ A vaga {vaga} foi atribuída "
            f"ao apartamento {proximo.id}."
        )


def menu_cadastro():

    print("""
=================================
    CADASTRO DE APARTAMENTO
=================================

1 - Cadastrar apartamento
2 - Listar apartamentos
3 - Remover apartamento
4 - Liberar vaga
5 - Listar fila de espera
6 - Listar vagas
0 - Sair

=================================
""")

    return int(input("Digite uma opção: "))


inicializar_vagas()

opcao = -1

while opcao != 0:

    opcao = menu_cadastro()

    if opcao == 1:

        cadastrar_apartamento()

    elif opcao == 2:

        print("\n--- Lista de apartamentos ---")
        lista.imprimir()

    elif opcao == 3:

        id_ap = int(
            input("Digite o ID do apartamento: ")
        )

        apartamento = lista.remover(id_ap)

        if apartamento is not None:
            liberar_vaga(apartamento.vaga)

            print(
                f"🔓 Vaga {apartamento.vaga} liberada!"
            )

    elif opcao == 4:

        liberar_vaga_apartamento()

    elif opcao == 5:

        print("\n--- Fila de espera ---")
        fila.imprimir()

    elif opcao == 6:

        print("\n--- Vagas do condomínio ---")
        vagas.imprimir()

    elif opcao == 0:

        print("Encerrando...")

    else:

        print("⚠️ Opção inválida!")