# Função sem parâmetro que retorna um dado
def getPI():
    return 3.14

# Função com parâmetro que retorna um dado 
def calcular_area(raio):
    area = raio * raio * getPI()
    return area

# Função com parâmetro que não retorna um dado
def imprimir_area_circulo(raio_):
    print(calcular_area(raio_))

def imprimir_pi():
    print(getPI())

# Execução vs referência
print("X e Y")
x = getPI()
y = getPI
print(x, y)

# PI
print("Valor do PI:")
imprimir_pi()
imprimir_area_circulo(4)