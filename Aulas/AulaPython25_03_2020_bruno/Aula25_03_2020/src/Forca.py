from operator import index

def main():

    print('*********************************')
    print('***Bem vindo ao jogo da Forca!***')
    print('*********************************')

    palavra_secreta = 'banana'
    acertou = False
    enforcou= False

    while (not acertou and not enforcou):
        chute = input('Qual letra?')
        posicao = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                print('Encontrei a letra {} na posição {}'.format(letra, index(posicao)))
            posicao = posicao + 1
if __name__ == "__main__":
    main()