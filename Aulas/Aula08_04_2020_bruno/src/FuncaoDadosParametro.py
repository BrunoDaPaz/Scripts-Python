def main():

    def dados(nome, idade=None):
        print('nome: {}'.format(nome))
        if(idade is not None):
            print('idade: {}'.format(idade))
        else:
            print("Idade Não Informada")

    #dados('Aula')
    dados('Aula2', 8)

if __name__ == "__main__":
    main()