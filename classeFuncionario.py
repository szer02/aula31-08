'''3. Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um
string) e um salário(um double). Escreva um construtor com dois parâmetros (nome e salário)
e métodos para devolver nome e salário. Escreva um pequeno programa que teste sua classe.
'''

'''4. Aprimore a classe do exercício anterior para adicionar o método aumentarSalario
(porcentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem.
Exemplo de uso:
harry=funcionário("Harry",25000)
harry.aumentarSalario(10)'''


class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def nome_funcionario(self):
        return self.nome

    def salario_funcionario(self):
        return self.salario
    
    def aumentar_salario(self, percentual_aumento):
        self.salario += (percentual_aumento / 100) * self.salario

nome = input('Digite o nome do funcionário: ')
salario = float(input('Digite o salário do funcionário: '))

funcionario1 = Funcionario(nome, salario)

nome_funcionario = funcionario1.nome_funcionario()
salario_funcionario = funcionario1.salario_funcionario()
salario_funcionario = "{:.3f}".format(salario_funcionario)

print(f'Nome do funcionário: {nome_funcionario}')
print(f'Salário do funcionário: {salario_funcionario}')

percentual_aumento = float(input('Digite o percentual de aumento de salário: '))
funcionario1.aumentar_salario(percentual_aumento)

print(f'Novo salário após aumento: {funcionario1.salario:.3f}')
