def main():

    def teste(variavel, *args):
        print('{}'.format(variavel))

        for controle in args:
            print('{}'.format(controle))

    teste('Argumento 1', 'Argumento 2', 'Argumento 3')

if __name__ == "__main__":
    main()