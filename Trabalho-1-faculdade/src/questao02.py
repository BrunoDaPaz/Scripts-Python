def main():

    listaNota = []
    nota = input('Informe sua primeira nota: ')
    listaNota += nota

    nota = input('Informe sua segunda nota: ')
    listaNota += nota

    nota = input('Informe sua terceira nota: ')
    listaNota += nota

    nota = input('Informe sua quarta e ultima nota: ')
    listaNota += nota

    print(listaNota)
    print("Sua maior nota é " + str(max(listaNota)))
    print("Sua menor nota é " + str(min(listaNota)))
    print("Sua média é " + sum(listaNota) / 4)



if __name__ == "__main__":
    main()
