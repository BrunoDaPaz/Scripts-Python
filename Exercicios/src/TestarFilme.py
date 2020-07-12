from src.Filme import Filme

if __name__ == '__main__':
    filme = Filme('Titanic', 'Titanic é um filme épico de romance e drama norte-americano de 1997, escrito, dirigido, co-produzido e co-editado por James Cameron', 193)

    filme.mostrarFilme(filme.titulo_filme, filme.resumo_filme)

    filme.horaMinuto(filme.duracao)
