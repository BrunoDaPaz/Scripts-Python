def main():

    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Stembro", "Outubro", "Novembro", "Dezembro"]
    print(meses)

    controlador = 1
    while(controlador < 4):

        #mes = input("Escolha um mês entre 1 e 12: ")
        mes = int(input("Escolha um mês entre 1 e 12 » "))
        if mes >= 1 and mes <= 12:
            print(meses[mes-1:])
            print(meses[mes-1:mes+2])
        controlador += 1
if __name__ == "__main__":
    main()