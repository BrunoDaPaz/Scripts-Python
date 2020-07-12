def main():


    arquivo = open('palavras.txt', 'r')
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    print(palavras)
    arquivo.close()

if __name__ == "__main__":
    main()