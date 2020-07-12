def main():

    numeros = []

    numero = input("Informe o primeiro número: ")
    numeros += numero
    numero = input("Informe o segundo número: ")
    numeros += numero
    numero = input("Informe o terceiro número: ")
    numeros += numero
    numero = input("Informe o quarto número: ")
    numeros += numero
    numero = input("Informe o quinto número: ")
    numeros += numero

    print(max(numeros))

if __name__ == "__main__":
    main()