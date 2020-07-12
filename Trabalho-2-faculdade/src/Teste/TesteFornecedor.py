from src.Fornecedor import Fornecedor

def main():

    fornecedor = Fornecedor('BRASPRESS', '74.814.418/0001-79', 'São Paulo', 'Rua Augusta, n° 142', 'BRASPRESS Transportadora')

    print('---------------------------------------')
    print('Nome: {}'.format(fornecedor.nome))
    print('CNPJ: {}'.format(fornecedor.cnpj))
    print('Cidade: {}'.format(fornecedor.cidade))
    print('Endereço: {}'.format(fornecedor.endereco))
    print('Razão Social: {}'.format(fornecedor.razaoSocial))
    print('---------------------------------------')

    # o método valida o CNPJ junto das pontuações.
    fornecedor.validaCNPJ(fornecedor.cnpj)

    fornecedor.agendarEntrega()

if __name__ == '__main__':
    main()