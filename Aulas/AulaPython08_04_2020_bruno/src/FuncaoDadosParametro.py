def main():

    def dados(nome, idade=None):
        print('Nome: {}'.format(nome))

        if(idade is not None):
           print('idade {}'.format(idade))

        else:
         print("Idade não informada")

        dados('bruno', 19)

if __name__ == "__main__":
    main()