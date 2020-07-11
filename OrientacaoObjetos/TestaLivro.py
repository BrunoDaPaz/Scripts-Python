from src.OrientacaoObjetos.Livro import Livro

def main():

    livro = Livro('Dom Quixote', 1300, 'Miguel de Cervantes', 399.90)
    livro.retornaPreco()
    livro.mudaPreco(299.90)
    livro.etiqueta()

if __name__ == '__main__':
    main()