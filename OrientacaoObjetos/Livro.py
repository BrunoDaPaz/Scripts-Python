class Livro:

    def __init__(self, nome, qtdPaginas, autor, preco):
        self._Nome = nome
        self._QtdPaginas = qtdPaginas
        self._Autor = autor
        self._Preco = preco

    @property
    def nome(self):
        return self._Nome
    @nome.setter
    def nome(self, nome):
        self._Nome = nome

    @property
    def qtdPaginas(self):
        return self._QtdPaginas
    @qtdPaginas.setter
    def qtdPaginas(self, qtdPaginas):
        self._QtdPaginas = qtdPaginas

    @property
    def autor(self):
        return self._Autor
    @autor.setter
    def autor(self, autor):
        self._Autor = autor

    @property
    def preco(self):
        return self._Preco
    @preco.setter
    def preco(self, preco):
        self._Preco = preco

    def retornaPreco(self):
        self._Preco

    def mudaPreco(self, preco):
        self._Preco = preco

    def etiqueta(self):
        print('Nome: {}'.format(self._Nome))
        print('Quantidade de Páginas: {}'.format(self._QtdPaginas))
        print('Autor: {}'.format(self._Autor))
        print('Preco: {}'.format(self._Preco))
