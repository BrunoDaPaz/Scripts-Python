from src.Gerente import Gerente

def main():

    gerente = Gerente('Bruno da Paz', '637.236.586.36', 15000, 'teste', 'teste', 'Gerente')
    print('-------------------------------------')

    print('Nome: {}'.format(gerente.nome))
    print('CPF: {}'.format(gerente.cpf))
    print('Salário: {}'.format(gerente.salario))
    print('Cargo: {}'.format(gerente.cargo))
    print('Usuário: {}'.format(gerente.usuario))
    print('Senha: {}'.format(gerente.senha))

    print('-------------------------------------')

    if (gerente.autentica(gerente.usuario, gerente.senha) and gerente.valida):

        print('-------------------------------------')
        gerente.bonificacao(2)

    #if (gerente.autentica('incorreto', 'incorreto')):
        #print('-------------------------------------')

if __name__ == '__main__':
    main()