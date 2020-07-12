import abc

#classe abstrada
class Funcionario(abc.ABC):

    #construtor da classe
    def __init__(self, nome, cpf, salario, cargo):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
        self._cargo = cargo

    #método abstrato
    @abc.abstractmethod
    def bonificacao(self):
        pass

    #método abstrato
    @abc.abstractmethod
    def autentica(self):
        pass

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def cpf(self):
        return self._cpf
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @property
    def salario(self):
        return self._salario
    @salario.setter
    def salario(self, salario):
        self._salario = salario

    @property
    def cargo(self):
        return self._cargo
    @cargo.setter
    def cargo(self, cargo):
        self._cargo = cargo
