from ListaVetores import ListaVetores

lista = ListaVetores()

for i in range(1, 16):
    lista.add(i)
    i += 1

lista.imprimir()

lista.busca_sequencial(7)
lista.busca_binaria(5)

lista.busca_sequencial(16)
lista.busca_binaria(-1)