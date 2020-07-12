from src.Funcionario import Funcionario
from src.Vendedor import Vendedor

def main():

    vendedor = Vendedor('Marcelo', '109.293.495-45', 3000.0, 'Vendedor', 'marcelo.vend', 'acb394', 3)

    print('-------------------------------------')

    print('Nome: {}'.format(vendedor.nome))
    print('CPF: {}'.format(vendedor.cpf))
    print('Salário: {}'.format(vendedor.salario))
    print('Cargo: {}'.format(vendedor.cargo))
    print('Usuário: {}'.format(vendedor.usuario))
    print('Senha: {}'.format(vendedor.senha))
    print('Vendas realizadas: {}'.format(vendedor.venda))

    print('-------------------------------------')

    if (vendedor.autentica(vendedor.usuario, vendedor.senha)):
        print('-------------------------------------')
        vendedor.bonificacao(vendedor.venda)

    #if (vendedor.autentica('incorreto', 'incorreto')):
        #print('-------------------------------------')
        #vendedor.bonificacao(vendedor.venda)

if __name__ == '__main__':
    main()