from src.Locacao import Locacao

def main():

    locacao = Locacao('2020-06-26', '', 250.00, '106.202.658-69', 1)

    print('---------------------------------------')
    print('Data de Saída: {}'.format(locacao.dataSaida))
    print('Data de Entrega: {}'.format(locacao.dataEntrega))
    print('Valor da Locacao: {}'.format(locacao.valorLocacao))
    print('Documento do Cliente: {}'.format(locacao.cpfCliente))
    print('Status da locação: {}'.format(locacao.status))
    print('---------------------------------------')


if __name__ == '__main__':
    main()