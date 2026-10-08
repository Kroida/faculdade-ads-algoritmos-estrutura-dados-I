def somarAte(n):
    if n < 1:
        print("Valor não permitido")
        return
    if n == 1:
        return 1
    else:
        return n + somarAte(n-1)

def somaPares(n):
    if n <= 1:
        return 0
    elif n % 2 == 1:
        return somaPares(n-1)
    else:
        return n + somaPares(n-2)

def fat(n):
    if n == 1:
        return 1
    else:
        return n * fat(n-1)

# 1)  Implemente uma função recursiva para cálculo de potência
def potencia(b, n):
    # if n == 1:
    #     return n
    if n == 0:
        return 1
    else:
        # return b ** potencia(b, (n-1))
        return b * potencia(b, (n-1))

# 2) Implemente um contador regressivo utilizando recursividade
import time

def contadorRegressivo(n):
    if n < 1:
        print("Valor não permitido")
        return

    print(n)
    time.sleep(1)

    if n == 1:
        return 1
    else:
        return contadorRegressivo(n-1)

# 3) Implemente uma função recursiva para inverter uma string
def inverterString( txt ):
    if len( txt ) == 1:
        return txt
    else:
        return inverterString( txt[ 1 : ] ) + txt[0]

#4) monte uma função que retur tru se a string informada for um palíndromo
def verificarPalindromo(txt, i = 0, j = None):
    if j is None:
        j = len(txt) - 1

    if i >= j:
        return True

    if txt[i] != txt[j]:
        return False

    return verificarPalindromo(txt, i + 1, j - 1)

# ---

n = int( input("Digite um número: "))
print( "A soma dos pares de 1 até ", n, " é: ", somaPares( n ) )
print( "A soma de 1 até ", n, " é: ", somarAte( n ) )
print( "O fatorial de ", n, " é: ", fat( n ) )
print( "2 elevado ao expoente ", n , " é: " , potencia(2, n) )
print("----------------------------")
contadorRegressivo(n)
print("----------------------------")
texto = input("Digite uma palavra: ")
print(inverterString(texto))
print(f"{texto} é um palíndromo" if verificarPalindromo(texto) == True else f"{texto} não é um palíndromo")