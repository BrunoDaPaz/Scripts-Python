from src.Funcionario import Funcionario

#classe gerente do tipo funcionário
class Gerente(Funcionario):

    #construtor da classe
    def __init__(self, nome, cpf, salario, cargo, usuario, senha):
        super().__init__(nome, cpf, salario, cargo)
        self._usuario = usuario
        self._senha = senha
        print('\n' + 'Gerente criado!')

    @property
    def usuario(self):
        return self._usuario
    @usuario.setter
    def usuario(self, usuario):
        self._usuario = usuario

    @property
    def senha(self):
        return self._senha
    @senha.setter
    def senha(self, senha):
        self._senha = senha

    #método
    def autentica(self, usuario, senha):
        if (self.senha == senha and self.usuario == usuario):
            print("Acesso permitido")
            return True
        else:
            print('Usuário ou Senha inválidos')
            return False

    #método
    def bonificacao(self, vendaParam):
        if (vendaParam <= 0):
            print('Sem bonificações, realize mais vendas!')
        elif (vendaParam <= 2):
            print('Bonificação do mês em cima da venda dos Vendedores: {}'.format(self._salario * 0.1) + '\n'
                  + 'Salário Atualizado: {}'.format(self._salario + (self._salario * 0.1)))
        elif (vendaParam > 2):
            print('Bonificação do mês em cima da venda dos Vendedores: {}'.format(self._salario * 0.25) + '\n'
                  + 'Salário Atualizado: {}'.format(self._salario + (self._salario * 0.25)))
