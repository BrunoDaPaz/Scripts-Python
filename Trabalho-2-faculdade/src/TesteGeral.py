from src.Funcionario import Funcionario
from src.Fornecedor import Fornecedor
from src.Locacao import Locacao
from src.Locadora import Locadora
from src.Veiculo import Veiculo
from src.Cliente import Cliente

def main():
    cliente = Cliente('Ragnar', '(47) 99182-7398', 'ragnar@hotmail.com', 'Progresso', '89045-345', 'Blumenau', '857.345.867-56', 'ragnar.wessex', 'abc345', '', 0)
    if (cliente.validaAtivo(cliente.ativo) and cliente.autentica(cliente.usuario, cliente.senha)):
        print('Bem-vindo {}\n'.format(cliente.nome))
        cliente.inserir()
        cliente.alterarSenha('testeCliente')

    funcionario = Funcionario('Pedro', '(47) 99102-9304', 'pedro@hotmail.com', 'Progresso', '89026-340', 'Blumenau', '304.918.345-32', 'pedro.funcionario', 'abc3422', 0, 0)
    if (funcionario.validaAtivo(funcionario.ativo) and funcionario.autentica(funcionario.usuario, funcionario.senha)):
        print('Bem-vindo {}\n'.format(funcionario.nome))
        funcionario.inserir()
        funcionario.alterarSenha('testeFuncionario')

    locacao = Locacao('2020-06-26', '', 250.00, '106.202.658-69', 1)
    locacao.inserir()

    veiculo = Veiculo('X5', 1, 'ABC1234', 'Ferrari', 'Vermelho', 'Sendan', 2020, 4, 0)
    veiculo.inserir()
    veiculo.validaNumeroRodas(veiculo.rodas)
    veiculo.validaAnoVeiculo(veiculo.ano)
    veiculo.validaStatus(veiculo.status)

    locadora = Locadora('LoCars', '80.314.123/0001-69', 'Blumenau', 'Rua Fernando de Noronha, n° 345', 'LoCaras Locadora')
    locadora.inserir()
    locadora.validaCNPJ(locadora.cnpj)

    fornecedor = Fornecedor('BRASPRESS', '74.814.418/0001-79', 'São Paulo', 'Rua Augusta, n° 142', 'BRASPRESS Transportadora')
    fornecedor.inserir()
    fornecedor.validaCNPJ(fornecedor.cnpj)
    fornecedor.agendarEntrega()



if __name__ == '__main__':
    main()