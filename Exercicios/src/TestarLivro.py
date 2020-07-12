from src.Livro import Livro

if __name__ == '__main__':
    livro = Livro('Bíblia', 590, 90)

    print("Nome atual do livro: " + livro.titulo_livro)
    livro.verificarProgresso(livro.quantidade_paginas, livro.paginas_lidas)

    livro.set_titulo_livro('O Pequeno Príncipe')
    print("Nome atual do livro: " + livro.get_titulo_livro())
    livro.set_quantidade_paginas(110)
    livro.verificarProgresso(livro.get_quantidade_paginas(), livro.get_paginas_lidas())
