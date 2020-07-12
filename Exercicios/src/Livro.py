class Livro:

    def __init__(self, titulo_livro, quantidade_paginas, paginas_lidas):
        self.titulo_livro = titulo_livro
        self.quantidade_paginas = quantidade_paginas
        self.paginas_lidas = paginas_lidas

    def get_titulo_livro(self):
        return self.titulo_livro
    def get_quantidade_paginas(self):
        return self.quantidade_paginas
    def get_paginas_lidas(self):
        return self.paginas_lidas

    def set_titulo_livro(self, titulo_livro):
        self.titulo_livro = titulo_livro
    def set_quantidade_paginas(self, quantidade_paginas):
        self.quantidade_paginas = quantidade_paginas
    def set_paginas_lidas(self, paginas_lidas):
        self.paginas_lidas = paginas_lidas

    def verificarProgresso(self, paramQuantidade_paginas, paramPaginas_lidas):
        percentual = round((paramPaginas_lidas * 100 / paramQuantidade_paginas))
        print('Você já leu {}% do livro'.format(percentual))