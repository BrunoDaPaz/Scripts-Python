class Pessoa:

    def __init__(self, nome, telefone, idade):
        self._Nome = nome
        self._Telefone = telefone
        self._Idade = idade

    @property
    def nome(self):
        return self._Nome
    @nome.setter
    def nome(self, nome):
        self._Nome = nome

    @property
    def telefone(self):
        return self._Telefone
    @telefone.setter
    def telefone(self, telefone):
        self._Telefone = telefone

    @property
    def idade(self):
        return self._Idade
    @idade.setter
    def idade(self, idade):
        self._Idade = idade

    def validaIdade(self, idade):
        if (idade < 18):
            print('{} é menor de idade.'.format(self._Nome))
        else:
            print('{} é maior de idade.'.format(self._Nome))