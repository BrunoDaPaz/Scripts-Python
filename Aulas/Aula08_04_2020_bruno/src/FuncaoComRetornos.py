def main():

    def calcularVelocidade(espaco, tempo):
        velocidade = espaco / tempo
        return velocidade

    resultado = calcularVelocidade(100, 20)
    print(resultado)

    print('--------------')

    def calcularVelocidade(espaco, tempo):
        velocidade = espaco / tempo
        if (velocidade is not None):
            return velocidade
        else:
            return 0

    valor = calcularVelocidade(100,20)
    print(valor)

if __name__ == "__main__":
    main()