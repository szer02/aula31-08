# 6. Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
'''OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de
combustível total na bomba.'''

class bombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        litros_abastecidos = valor / self.valorLitro
        if litros_abastecidos <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litros_abastecidos
            return f'Você abasteceu {litros_abastecidos:.2f} litros de {self.tipoCombustivel}'
        else:
            return 'Quantidade de combustível insuficiente na bomba'

    def abastecerPorLitro(self, litros):
        valor_a_pagar = litros * self.valorLitro
        if litros <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litros
            return f'Valor a pagar: R$ {valor_a_pagar:.2f}'
        else:
            return 'Quantidade de combustível insuficiente na bomba'

    def alterarValor(self, novo_valor_litro):
        self.valorLitro = novo_valor_litro
        return f'Valor do litro de {self.tipoCombustivel} alterado para R$ {self.valorLitro:.2f}'

    def alterarCombustivel(self, novo_tipo_combustivel):
        self.tipoCombustivel = novo_tipo_combustivel
        return f'Tipo de combustível alterado para {self.tipoCombustivel}'

    def alterarQuantidadeCombustivel(self, nova_quantidade):
        self.quantidadeCombustivel = nova_quantidade
        return f'Quantidade de combustível na bomba alterada para {self.quantidadeCombustivel} litros'

    def mostrarQuantidadeAtual(self):
        return f'Quantidade atual na bomba: {self.quantidadeCombustivel:.2f} litros'

# Solicitar valores ao usuário
tipo_combustivel = input('Digite o tipo de combustível: ')
valor_litro = float(input('Digite o valor por litro: '))
quantidade_combustivel = float(input('Digite a quantidade de combustível na bomba: '))

# Criar a bomba com os valores informados
bomba = bombaCombustivel(tipo_combustivel, valor_litro, quantidade_combustivel)

# Menu de operações
while True:
    print('\nEscolha uma operação:')
    print('1 - Abastecer por valor')
    print('2 - Abastecer por litro')
    print('3 - Alterar valor do litro')
    print('4 - Alterar tipo de combustível')
    print('5 - Alterar quantidade de combustível na bomba')
    print('6 - Mostrar quantidade atual na bomba')
    print('7 - Sair')
    
    opcao = input('Opção: ')

    if opcao == '1':
        valor_abastecimento = float(input('Digite o valor a ser abastecido: '))
        print(bomba.abastecerPorValor(valor_abastecimento))
    elif opcao == '2':
        litros_abastecimento = float(input('Digite a quantidade em litros a ser abastecida: '))
        print(bomba.abastecerPorLitro(litros_abastecimento))
    elif opcao == '3':
        novo_valor_litro = float(input('Digite o novo valor por litro: '))
        print(bomba.alterarValor(novo_valor_litro))
    elif opcao == '4':
        novo_tipo_combustivel = input('Digite o novo tipo de combustível: ')
        print(bomba.alterarCombustivel(novo_tipo_combustivel))
    elif opcao == '5':
        nova_quantidade_combustivel = float(input('Digite a nova quantidade de combustível na bomba: '))
        print(bomba.alterarQuantidadeCombustivel(nova_quantidade_combustivel))
    elif opcao == '6':
        print(bomba.mostrarQuantidadeAtual())
    elif opcao == '7':
        break
    else:
        print('Opção inválida. Tente novamente.')
