def main():

    valores = [1,2,-4, 5,8,4]
    print(type(valores))
    print(min(valores))
    print(max(valores))

    valoresLetras = ['a', 'b', 'f']
    print(min(valoresLetras))
    print(max(valoresLetras))

    print(valores[0])
    valores[2] = 10
    valores[5] = 1
    print('Nova Lista: ' + str(valores))

    print(len(valores))
    print(10 in valores)

    valores.append(100) ## add ao final da lista
    print(valores)

    valores.pop(2) ##remove na posição 2
    print(valores)

if __name__ == "__main__":
    main()