from src.Funcionario import Funcionario

#classe vendedor do tipo funcionário
class Vendedor(Funcionario):

    #construtor da classe
    def __init__(self, nome, cpf, salario, cargo, usuario, senha, venda):
        super().__init__(nome, cpf, salario, cargo)
        self._usuario = usuario
        self._senha = senha
        self._venda = venda
        print('\n' + 'Vendedor criado!')

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

    @property
    def venda(self):
        return self._venda
    @venda.setter
    def venda(self, venda):
        self._venda = venda

    #método
    def bonificacao(self, venda):
        if (venda <= 0):
            print('Sem bonificações, realize mais vendas!')
        elif (venda <= 2 ):
            print('Bonificação do mês: {}'.format(self._salario * 0.2) + '\n'
                  + 'Salário Total: {}'.format(self._salario + (self._salario * 0.2)))
        elif (venda > 2):
            print('Bonificação do mês: {}'.format(self._salario * 0.5) + '\n'
                  + 'Salário Total: {}'.format(self._salario + (self._salario * 0.5)))

    #método
    def autentica(self, usuario, senha):
        if (self.senha == senha and self.usuario == usuario):
            print("Acesso permitido")
            return True
        else:
            print('Usuário ou Senha inválidos')
            return False