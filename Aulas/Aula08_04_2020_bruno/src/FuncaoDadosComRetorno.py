def main():

    def dados(nome, idade=None):
        if (idade is not None):
            #return ('nome: {} e idade: {}'.format(nome, idade))
            return("Nome: " + str(nome) + " - Idade: " + str(idade))
        else:
            return("Nome: " + str(nome))

    valor = dados("Teste", 20)
    print(valor)


    novoValor = dados("Teste")
    print(novoValor)


if __name__ == "__main__":
    main()