def main():

    def minhaFuncao(**kwargs):

        for variavel, valor in kwargs.items():
            print('{0} = {1}'.format(variavel, valor))

    minhaFuncao(nome='franciela', idade = 10, corCabelo = 'rosa')

if __name__ == "__main__":
    main()