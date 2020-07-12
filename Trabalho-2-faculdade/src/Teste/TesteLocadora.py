from src.Locadora import Locadora

def main():

    locadora = Locadora('LoCars', '80.314.123/0001-69', 'Blumenau', 'Rua Fernando de Noronha, n° 345', 'LoCaras Locadora')

    print('---------------------------------------')
    print('Nome: {}'.format(locadora.nome))
    print('CNPJ: {}'.format(locadora.cnpj))
    print('Cidade: {}'.format(locadora.cidade))
    print('Endereço: {}'.format(locadora.endereco))
    print('Razão Social: {}'.format(locadora.razaoSocial))
    print('---------------------------------------')

    locadora.validaCNPJ(locadora.cnpj)

if __name__ == '__main__':
    main()