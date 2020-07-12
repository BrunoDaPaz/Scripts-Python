from src.Empresa import Empresa
import datetime

class Fornecedor(Empresa):

    def __init__(self, nome, cnpj, cidade, endereco, razaoSocial):
        super().__init__(nome, cnpj, cidade, endereco, razaoSocial)
        print('\n>Fornecedor Criado<')

    def validaCNPJ(self, cnpj):
        if len(cnpj) == 18:
            print('CNPJ válido.')
            print('---------------------------------------')
        else:
            raise ValueError("Quantidade de digitos inválida")
            print('---------------------------------------')

    def agendarEntrega(self):
        datetime.date = input('Informe a data no formato yyyy-mm-dd: ')
        print('Entrega agendada para {}'.format(datetime.date))
        print('---------------------------------------')

    def inserir(self):
        print('---------------------------------------')
        print('Nome: {}'.format(self.nome))
        print('CNPJ: {}'.format(self.cnpj))
        print('Cidade: {}'.format(self.cidade))
        print('Endereço: {}'.format(self.endereco))
        print('Razão Social: {}'.format(self.razaoSocial))
        print('---------------------------------------')