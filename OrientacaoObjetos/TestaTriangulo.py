from src.OrientacaoObjetos.Triangulo import Triangulo

def main():

    ladoA = int(input('Informe a medida do primeiro lado (A) do triângulo: '))
    ladoB = int(input('Informe a medida do segundo lado (B) do triângulo: '))
    ladoC = int(input('Informe a medida do terceiro lado (C) do triângulo: '))

    triangulo = Triangulo(ladoA, ladoB, ladoC)
    triangulo.calcularPerimetro(ladoA, ladoB, ladoC)
    triangulo.getMaiorlado()

if __name__ == '__main__':
    main()