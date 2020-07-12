def main():

    def dados(nome, idade=None):
        print('nome: {}'.format(nome))
        if (idade is not None):
            print('idade: {}'.format(idade))
        else:
            print('idade: não informada')

    dados('Franciela', 34)
    dados('Nissola')
    dados(34)
    dados(idade=34)

if __name__ == "__main__":
    main()