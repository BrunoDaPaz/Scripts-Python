def main():

    nome = input('Informe o seu nome: ')
    senha  = input('Informe uma senha: ')

    if senha == nome:
        print("Erro!!!")
        print("A senha não pode ser a mesma informação do usuário.")
        return main()
    else :
        print("Cadastro realizado com sucesso.")

if __name__ == "__main__":
    main()