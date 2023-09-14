'''2. Classe Quadrado: Crie uma classe que modele um quadrado:
I. Atributos: Tamanho do lado
II. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;'''


class Quadrado:
    def __init__(self, tLado):
        self.tLado = tLado

    def mudar_lado (self):
        novoLado = input(f'Digite um novo lado: ')

        if novoLado.isdigit(): #Vericica se o valor atribuido é string
            self.tLado = int(novoLado)
            return self.tLado
        
        else:
            print('Digite apenas números.')

    def valor_lado (self):
        print(f'O valor atual do lado é: {self.tLado}')

    def calcular_area (self):
        area = self.tLado * self.tLado
        print(f'O valor do lado é {self.tLado} e área total possui {area} cm²')

square = Quadrado(0)

Quadrado.mudar_lado(square)
Quadrado.valor_lado(square)
Quadrado.calcular_area(square)



