from src.Veiculo import Veiculo

def main():

    veiculo = Veiculo('Sandero', 'Carro', 'abc1234', 'Renault', 'Preto', 1)

    print('-------------------------------------')

    print('Nome: {}'.format(veiculo.nome))
    print('Tipo: {}'.format(veiculo.tipo))
    print('Placa: {}'.format(veiculo.placa))
    print('Marca: {}'.format(veiculo.marca))
    print('Cor: {}'.format(veiculo.cor))

    print('-------------------------------------')

    veiculo.validaStatus(veiculo.status)

if __name__ == '__main__':
    main()