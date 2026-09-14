from Fila import Fila

fifo = Fila()
fifo.imprimir()
fifo.add( "João" )
fifo.add( "Maria" )
fifo.add( "Bibiana" )
fifo.add( "José" )
print("===============================")
fifo.remover()
fifo.remover()
fifo.remover()
fifo.add("Miguel")


#Exercício:
# Construa um aplicativo para um lava-jato de carros
# em que o carro possui placa e ano.
# Devem ser construídos os seguintes métodos:
# 1) Adicionar carro na fila
# 2) Lavar carro (remover)
# 3) Imprimir a fila de carros
# 4) Retornar a posição na fila ao informar a placa
# 5) Sair
# Construa um menu de opções com as opções acima citadas
# O aplicativo só termina quando o usuário escolher a opção 5
