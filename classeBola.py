'''1. Classe Bola: Crie uma classe que modele uma bola:
a. Atributos: Cor, circunferência, material
b. Métodos: trocaCor e mostraCor'''


class Bola:
    def __init__(self, cor, circuferencia, material):
        self.cor = cor
        self.circuferencia = circuferencia
        self.material = material

    def TrocaCor (self):
        troca = input(f'Deseja troca a cor atual {self.cor}? (s/n): ')
        troca = troca[0].lower()

        if troca == 's':
            self.cor = input(f'Digite a nova cor: ')
            return self.cor

        else:
            print(f'A cor {self.cor} não foi alterada!')

    def MostraCor(self):
        print(f'A cor atual é {self.cor}')

ball = Bola('Rosa', 5, 'Metal')
Bola.TrocaCor(ball)
Bola.MostraCor(ball)

    