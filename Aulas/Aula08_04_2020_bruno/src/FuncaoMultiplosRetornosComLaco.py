def main():

    def calculadora(x, y):
        return {'soma ':x+y, 'subtração ': x-y}


    resultados = (calculadora(1,2))
    print(type(resultados))

    for key in resultados:
        print('{}: {}'.format(key, resultados[key]))

if __name__ == "__main__":
    main()