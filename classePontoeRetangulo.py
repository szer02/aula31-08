# 5. Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:

# a) Possua uma classe chamada Ponto, com os atributos x e y.
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
# c) Possua uma função para imprimir os valores da classe Ponto
    def imprime_valores(self):
        print(f'Ponto: ({self.x}, {self.y})')

# b) Possua uma classe chamada Retangulo, com os atributos largura e altura.
# f) Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo
# do retângulo, que deve ser um objeto da classe Ponto.
class Retangulo():
    def __init__(self, largura, altura, ponto_inicial):
        self.largura = largura
        self.altura = altura
        self.ponto_inicial = ponto_inicial

# d) Possua uma função para encontrar o centro de um Retângulo.
# g) A função para encontrar o centro do retângulo deve retornar o valor para um objeto do
# tipo ponto que indique os valores de x e y para o centro do objeto.
    def encontrar_centro(self):
        x_centro = (self.ponto_inicial.x + self.largura) / 2
        y_centro = (self.ponto_inicial.y + self.altura) / 2
        return x_centro, y_centro

# i) Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.
def menu():
    largura = float(input('Digite a largura do retangulo: '))
    altura = float(input('Digite a altura do retangulo: '))
    x_ponto = float(input('Digite a coordenada x do ponto inicial: '))
    y_ponto = float(input('Digite a coordenada y do ponto inicial: '))

    ponto_inicial = Ponto(x_ponto, y_ponto)
    retangulo = Retangulo(largura, altura, ponto_inicial)

    print('\n Informações do retângulo: ')
    ponto_inicial.imprime_valores()

    print(f'Largura: {retangulo.largura}')
    print(f'Altura: {retangulo.altura}')

# h) O valor do centro do objeto deve ser mostrado na tela
    centro = retangulo.encontrar_centro()
    print('\nCentro do Retângulo:')
    print(centro)

menu()