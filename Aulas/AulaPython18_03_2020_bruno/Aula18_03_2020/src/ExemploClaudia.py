def main():
#  Pode ser assim com o "f" na frente das aspas e as variaveis dentro das chaves
    nome = "Franciela"
    sobrenome = "Nissola"
    idade =  18

    print(f"O nome digitado foi {nome} {sobrenome}")

#  Ou pode ser assim, que é mais legal, com o "%s", "%d" e as variaveis dentro dos parenteses

    print("O nome digitado foi {%s} {%s} {%d}" % (nome,sobrenome,idade))

if __name__ == "__main__":
    main()
