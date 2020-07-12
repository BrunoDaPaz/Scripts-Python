def main():

    def teste(arg, *args):
        print('primeiro argumento normal: {}'.format(arg))

        for variavel in args:
            print('outro argumento: {}'.format(variavel))

    teste('python', 'é', 'muito', 'legal')

    print('------------')
    lista = ["é", "muito", "legal"]
    teste('python', *lista)

if __name__ == "__main__":
    main()