from src.Empresa import Empresa

class Locadora(Empresa):

    def __init__(self, nome, cnpj, cidade, endereco, razaoSocial):
        super().__init__(nome, cnpj, cidade, endereco, razaoSocial)
        print('\n>Locadora Criado<')

    def validaCNPJ(self, cnpj):
        if len(cnpj) == 18:
            print('CNPJ válido.')
            print('---------------------------------------')
        else:
            raise ValueError("Quantidade de digitos inválida")
            print('---------------------------------------')

    def inserir(self):
        print('---------------------------------------')
        print('Nome: {}'.format(self.nome))
        print('CNPJ: {}'.format(self.cnpj))
        print('Cidade: {}'.format(self.cidade))
        print('Endereço: {}'.format(self.endereco))
        print('Razão Social: {}'.format(self.razaoSocial))
        print('---------------------------------------')