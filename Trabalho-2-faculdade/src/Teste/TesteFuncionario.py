from src.Funcionario import Funcionario

def main():

    funcionario = Funcionario('Pedro', '(47) 99102-9304', 'pedro@hotmail.com', 'Progresso', '89026-340',
                              'Blumenau', '304.918.345-32', 'pedro.funcionario', 'abc3422', 0, 0)

    print('---------------------------------------')
    print('Nome: {}'.format(funcionario.nome))
    print('Telefone: {}'.format(funcionario.telefone))
    print('E-mail: {}'.format(funcionario.email))
    print('Bairro: {}'.format(funcionario.bairro))
    print('CEP: {}'.format(funcionario.cep))
    print('Cidade: {}'.format(funcionario.cidade))
    print('CPF: {}'.format(funcionario.cpf))
    print('Nome de Usuário: {}'.format(funcionario.usuario))
    print('Senha: {}'.format(funcionario.senha))
    print('Pontuação: {}'.format(funcionario.pontuacao))
    print('Status: {}'.format(funcionario.ativo))
    print('---------------------------------------')

    if(funcionario.validaAtivo(funcionario.ativo) and funcionario.autentica(funcionario.usuario, funcionario.senha)):

        print('Bem vindo {}\n'.format(funcionario.nome))

        # método para alterar senha de usuário
        funcionario.alterarSenha(input('Insira uma nova senha de acesso: '))

if __name__ == '__main__':
    main()