def main():

    print("-------------Uso do Comando ELIF ")

    variavel = 10
    chute = 2


    if chute == variavel:
        print("Acerto!!!")
    elif(chute > variavel):
            print("Chute maior que a variavel")
    elif(chute < variavel):
            print("Chute menor que a variavel")

if __name__ == "__main__":
    main()