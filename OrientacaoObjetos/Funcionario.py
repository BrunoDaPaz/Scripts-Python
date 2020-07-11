class Funcionario:

    def __init__(self, nome, salario):
        self._Nome = nome
        self._Salario = salario

    @property
    def nome(self):
        return self._Nome
    @nome.setter
    def nome(self, nome):
        self._Nome = nome

    @property
    def salario(self):
        return self._Salario
    @salario.setter
    def salario(self, salario):
        self._Salario = salario

    def aumentarSalario(self, percentualDeAumento):
        self._Salario += (percentualDeAumento / 100) * self._Salario
