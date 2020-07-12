from src.Retangulo import Retangulo

if __name__ == '__main__':
    retangulo = Retangulo(5, 10)
    print('Valor do lado 1: ', str(retangulo))
    print('Valor do lado 2: ', str(retangulo))

    retangulo.calcularArea(retangulo.lado1, retangulo.lado2)
    print('A área do retangulo é de: ', str(retangulo.area))

    retangulo.calcularPerimetro(5, 10)
    print('O perímetro do retangulo é de: ', str(retangulo.perimetro))