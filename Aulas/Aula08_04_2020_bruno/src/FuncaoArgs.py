def main():

    def teste(variavel, *args):
        print('Primeiro Argumento:{}'.format(variavel))

        for controle in args:
            print('outros argumento: {}'.format(controle))

    teste('Variavel 1', 'A', 'B', 'C', 'D')

if __name__ == "__main__":
    main()