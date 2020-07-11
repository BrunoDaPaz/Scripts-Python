from src.HerancaPolimorfismo.Pessoa import Pessoa

class Funcionario(Pessoa):

    def __init__(self, nome, telefone, idade, salario, usuario, senha):
        super().__init__(nome, telefone, idade)
        self._Salario = salario
        self._Usuario = usuario
        self._Senha = senha

    @property
    def salario(self):
        return self._Salario
    @salario.setter
    def salario(self, salario):
        self._Salario = salario

    @property
    def usuario(self):
        return self._Usuario
    @usuario.setter
    def usuario(self, usuario):
        self._Usuario = usuario

    @property
    def senha(self):
        return self._Senha
    @senha.setter
    def senha(self, senha):
        self._Senha = senha

    def validaIdade(self, idade):
        if (idade <  65):
            print('{} não é aposentado.'.format(self._Nome))
        else:
            print('{} é aposentado.'.format(self._Nome))
