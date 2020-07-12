from src.Empregado import Empregado

if __name__ == '__main__':
    empregado = Empregado('bruno', 'da paz', 5000)
    print('Seu primeiro nome: ', str(empregado.primeiro_nome))
    print('Seu sobrenome: ', str(empregado.sobrenome))
    print('Seu salário mensal: ', str(empregado.salario_mensal))

    empregado.nomeCompleto(empregado.primeiro_nome, empregado.sobrenome)
    print('Nome completo: ' + str(empregado.nome_completo))

    empregado.extrato(empregado.nome_completo, empregado.salario_mensal)
    print('Extrato do empregado: ' + str(empregado.extratoEmpregado))

    empregado.aumentarSalario(5)
    print('Salário reajustado: ' + str(empregado.salarioReajustado))

    empregado2 = Empregado('fran', 'da paz', 7500)
    print('\n' + 'Seu primeiro nome: ', str(empregado2.primeiro_nome))
    print('Seu sobrenome: ', str(empregado2.sobrenome))
    print('Seu salário mensal: ', str(empregado2.salario_mensal))

    empregado2.nomeCompleto(empregado2.primeiro_nome, empregado2.sobrenome)
    print('Nome completo: ' + str(empregado2.nome_completo))

    empregado2.extrato(empregado2.nome_completo, empregado2.salario_mensal)
    print('Extrato do empregado: ' + str(empregado2.extratoEmpregado))

    empregado2.aumentarSalario(5)
    print('Salário reajustado: ' + str(empregado2.salarioReajustado))