def main():

    def minha_funcao(**kwargs):
        for variavel, valor in kwargs.items():
            print('{0} = {1}'.format(variavel, valor))

    dicionario = {'nome': 'joao', 'idade': 25}
    minha_funcao(**dicionario)

if __name__ == "__main__":
    main()