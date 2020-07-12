from src.Veiculo import Veiculo

def main():

    veiculo = Veiculo('X5', 0, 'ABC1234', 'Ferrari', 'Vermelho', 'Sendan', 2010, 4, 1)

    print('---------------------------------------')
    print('Nome: {}'.format(veiculo.nome))
    print('Tipo de veículo: {}'.format(veiculo.tipo))
    print('Placa: {}'.format(veiculo.placa))
    print('Marca: {}'.format(veiculo.marca))
    print('Cor: {}'.format(veiculo.cor))
    print('Modelo: {}'.format(veiculo.modelo))
    print('Ano: {}'.format(veiculo.ano))
    print('Número de rodas: {}'.format(veiculo.rodas))
    print('Status: {}'.format(veiculo.status))
    print('---------------------------------------')

    if(veiculo.validaAnoVeiculo(veiculo.ano) and veiculo.validaNumeroRodas(veiculo.rodas)):
            print('TESTE VALIDAÇÃO')

if __name__ == '__main__':
    main()