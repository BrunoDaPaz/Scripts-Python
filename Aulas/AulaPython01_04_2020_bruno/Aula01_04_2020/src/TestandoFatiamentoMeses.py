def main():

    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio','Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

    controlador = 1
    while(controlador < 4):
        mes = input("Escolha um mês (entre 1 e 12): ")
        if int(mes) >= 1 and int(mes) <= 12:
            converteMes = int(mes) - 1
            print(meses[int(converteMes) : int(converteMes + 2)])
        controlador = controlador + 1

if __name__ == "__main__":
    main()