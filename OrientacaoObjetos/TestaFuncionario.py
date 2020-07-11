from src.OrientacaoObjetos.Funcionario import  Funcionario

def main():

    nome = input('Informe o seu nome: ')
    salario = int(input('Informe o seu salário: '))
    print('-------------------------------------')

    funcionario = Funcionario(nome, salario)
    print('Nome do funcionário informado: {}'.format(funcionario.nome))
    print('Salário inicial: {}'.format(funcionario.salario))
    print('-------------------------------------')

    funcionario.aumentarSalario(8)
    print('Salário com aumento: {}'.format(funcionario.salario))
    print('-------------------------------------')

if __name__ == '__main__':
    main()