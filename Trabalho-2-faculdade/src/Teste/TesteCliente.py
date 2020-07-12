from src.Cliente import Cliente

def main():

    cliente = Cliente('Ragnar', '(47) 99182-7398', 'ragnar@hotmail.com', 'Progresso', '89045-345', 'Blumenau',
                      '857.345.867-56', 'ragnar.wessex', 'abc345', '', 0)

    print('---------------------------------------')
    print('Nome: {}'.format(cliente.nome))
    print('Telefone: {}'.format(cliente.telefone))
    print('E-mail: {}'.format(cliente.email))
    print('Bairro: {}'.format(cliente.bairro))
    print('CEP: {}'.format(cliente.cep))
    print('Cidade: {}'.format(cliente.cidade))
    print('CPF: {}'.format(cliente.cpf))
    print('Usuario: {}'.format(cliente.usuario))
    print('Senha: {}'.format(cliente.senha))
    print('CNPJ: {}'.format(cliente.cnpj))
    print('Status: {}'.format(cliente.ativo))
    print('---------------------------------------')

    # teste usuário com senha ou usuário errados
    #if (cliente.validaAtivo(cliente.ativo) and cliente.autentica('ragnar.uecex', cliente.senha)):
        #cliente.alterarSenha('abc343')

    # teste usuário inativo
    #if (cliente.validaAtivo(cliente2.ativo) and cliente.autentica(cliente2.usuario, cliente2.senha)):
        #cliente.alterarSenha('abc343')

    # teste usuário correto
    if (cliente.validaAtivo(cliente.ativo) and cliente.autentica(cliente.usuario, cliente.senha)):
        print('Bem-vindo {}\n'.format(cliente.nome))
        cliente.alterarSenha(input('Insira uma nova senha de acesso: '))

if __name__ == '__main__':
    main()