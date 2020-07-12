import abc

class Pessoa(abc.ABC):

    def __init__(self, nome, telefone, email, bairro, cep, cidade, cpf):
        self._nome = nome
        self._telefone = telefone
        self._email = email
        self._bairro = bairro
        self._cep = cep
        self._cidade = cidade
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def telefone(self):
        return self._telefone
    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, email):
        self.email = email

    @property
    def bairro(self):
        return self._bairro
    @bairro.setter
    def bairro(self, bairro):
        self._bairro = bairro

    @property
    def cep(self):
        return self._cep
    @cep.setter
    def cep(self, cep):
        self._cep = cep

    @property
    def cidade(self):
        return self._cidade
    @cidade.setter
    def cidade(self, cidade):
        self._cidade = cidade

    @property
    def cpf(self):
        return self._cpf
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @abc.abstractmethod
    def validaAtivo(self, param1):
        pass

    @abc.abstractmethod
    def autentica(self, param1, param2):
        pass