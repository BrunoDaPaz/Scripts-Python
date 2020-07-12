from operator import index

def main():
    print('**************************')
    print('******Jogo da Forca*******')
    print('**************************')

    palavra_secreta = 'AulaDeHoje'
    lista = []
    print(type(lista))

    acertou = False
    enforcou = False

    while(not acertou and not enforcou):
        chute = input("Qual letra?")
        posicao = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                print("Acertou!!!Encontrei {} na posição {}: ".format(letra, index(posicao)))
            posicao = posicao + 1
        else:
                print("Errooouuu (leia com voz do Faustão!!")

    print("Fim do Jogo")
if __name__ == "__main__":
    main()