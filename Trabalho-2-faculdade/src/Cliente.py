from src.Pessoa import Pessoa
from src.Enum.EnumAtivo import EnumAtivo

class Cliente(Pessoa):

    def __init__(self, nome, telefone, email, bairro, cep, cidade, cpf, usuario, senha, cnpj, ativo):
        super().__init__(nome, telefone, email, bairro, cep, cidade, cpf)
        self._usuario = usuario
        self._senha = senha
        self._cnpj = cnpj
        self._ativo = EnumAtivo(ativo)
        print('\n>Cliente Criado<')

    @property
    def usuario(self):
        return self._usuario
    @usuario.setter
    def usuario(self, usuario):
        self._usuario = usuario

    @property
    def senha(self):
        return self._senha
    @senha.setter
    def senha(self, senha):
        self._senha = senha

    @property
    def cnpj(self):
        return self._cnpj
    @cnpj.setter
    def cnpj(self, cnpj):
        self._cnpj = cnpj

    @property
    def ativo(self):
        return self._ativo
    @ativo.setter
    def ativo(self, ativo):
        self._ativo = ativo

    def validaAtivo(self, status):
        if (EnumAtivo.Ativo == status):
            print('---------------------------------------')
            print('VALIDAÇÃO: Usuário Ativo.')
            print('---------------------------------------')
            return True
        elif (EnumAtivo.Inativo == status):
            print('---------------------------------------')
            print('VALIDAÇÃO: Usuário inativo, constate o usuário administrador.')
            print('---------------------------------------')
            return False

    def alterarSenha(self, senha):
        if(senha == self.senha):
            print('A senha não pode ser a mesma da atual!')
            print('---------------------------------------')
            return False
        else:
            self._senha = senha
            print('Senha alterada para: {}'.format(self._senha))
            print('---------------------------------------')

    def autentica(self, usuario, senha):
        if (self.senha == senha and self.usuario == usuario):
            print("Acesso permitido")
            print('---------------------------------------')
            return True
        else:
            print('Usuário ou Senha inválidos')
            print('---------------------------------------')
            return False

    def inserir(self):
        print('Nome: {}'.format(self.nome))
        print('Telefone: {}'.format(self.telefone))
        print('E-mail: {}'.format(self.email))
        print('Bairro: {}'.format(self.bairro))
        print('CEP: {}'.format(self.cep))
        print('Cidade: {}'.format(self.cidade))
        print('CPF: {}'.format(self.cpf))
        print('Usuario: {}'.format(self.usuario))
        print('Senha: {}'.format(self.senha))
        print('CNPJ: {}'.format(self.cnpj))
        print('Status: {}'.format(self.ativo))
        print('---------------------------------------')