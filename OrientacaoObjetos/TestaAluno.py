from src.OrientacaoObjetos.Aluno import Aluno

def main():

    aluno = Aluno('Bruno', 'TSI', 0)

    opcao = 0  # 1 - Estudar / 2 = Dormir / 3 - Encerrar
    while opcao != 3:
        try:
            opcao = int(input('\nSelecione uma opção abaixo\n'
                  '1 - Estudar'
                  '\n2 - Dormir'
                  '\n3 - Encerrar: '))

            if (opcao == 1):
                horasEstudar = int(input('Informe quantas horas vai estudar: '))
                aluno.estudar(horasEstudar)
            elif (opcao == 2):
                horasDormir = int(input('Informe quantas horas vai dormir: '))
                aluno.dormir(horasDormir)
            elif(opcao > 3):
                print('\nOpção inválida!')
        except:
            print('\nFavor informar uma opção válida (1, 2 ou 3).')

    print('\nHoras sem dormir: {}:00'.format(aluno.tempoSemDormir))

if __name__ == '__main__':
    main()