class Empregado:

    def __init__(self, primeiro_nome, sobrenome, salario_mensal):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome
        self.salario_mensal = salario_mensal

    def get_primeiro_nome(self):
        return self.primeiro_nome
    def get_sobrenome(self):
        return self.sobrenome
    def get_salario_mensal(self):
        return self.salario_mensal

    def set_primeiro_nome(self, primeiro_nome):
        self.primeiro_nome = primeiro_nome
    def set_sobrenome(self, sobrenome):
        self.sobrenome = sobrenome
    def set_salario_mensal(self, salario_mensal):
        self.salario_mensal = salario_mensal

    def nomeCompleto(self, paramPrimeiroNome, paramSobrenome):
        self.nome_completo = (paramPrimeiroNome + ' ' + paramSobrenome)

    def extrato(self, paramNomeCompleto, paramSalarioMensal):
        self.extratoEmpregado = (paramNomeCompleto + ' - Salário R$' + str(float(paramSalarioMensal)))

    def aumentarSalario(self, percentual):
        self.reajuste = (percentual / 100) * self.salario_mensal
        self.salarioReajustado = self.reajuste + self.salario_mensal