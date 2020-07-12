import abc

class Empresa(abc.ABC):

        def __init__(self, nome, cnpj, cidade, endereco, razaoSocial):
            self._nome = nome
            self._cnpj = cnpj
            self._cidade = cidade
            self._endereco = endereco
            self._razaoSocial = razaoSocial

        @property
        def nome(self):
            return self._nome
        @nome.setter
        def nome(self, nome):
            self._nome = nome

        @property
        def cnpj(self):
            return self._cnpj
        @cnpj.setter
        def cnpj(self, cnpj):
            self._cnpj = cnpj

        @property
        def cidade(self):
            return self._cidade
        @cidade.setter
        def cidadej(self, cidade):
            self._cidade = cidade

        @property
        def endereco(self):
            return self._endereco
        @endereco.setter
        def endereco(self, endereco):
            self._endereco = endereco

        @property
        def razaoSocial(self):
            return self._razaoSocial
        @razaoSocial.setter
        def razaoSocial(self, razaoSocial):
            self._razaoSocial = razaoSocial

        def validaCNPJ(self, cnpj):
            pass
