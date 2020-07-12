from src.Enum.EnumLocacao import EnumLocacao

class Locacao:

    def __init__(self, dataSaida, dataEntrega, valorLocacao, cpfCliente, status):
        self._dataSaida = dataSaida
        self._dataEntrega = dataEntrega
        self._valorLocacao = valorLocacao
        self._cpfCliente = cpfCliente
        self._status = EnumLocacao(status)
        print('\n>Locacao Criada<')

    @property
    def dataSaida(self):
        return self._dataSaida
    @dataSaida.setter
    def dataSaida(self, dataSaida):
        self._dataSaida = dataSaida

    @property
    def dataEntrega(self):
        return self._dataEntrega
    @dataEntrega.setter
    def dataEntrega(self, dataEntrega):
        self._dataEntrega = dataEntrega

    @property
    def valorLocacao(self):
        return self._valorLocacao
    @valorLocacao.setter
    def valorLocacao(self, valorLocacao):
        self._valorLocacao = valorLocacao

    @property
    def cpfCliente(self):
        return self._cpfCliente
    @cpfCliente.setter
    def nome(self, cpfCliente):
        self._cpfCliente = cpfCliente

    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, status):
        self._status = status

    def inserir(self):
        print('---------------------------------------')
        print('Data de Saída: {}'.format(self.dataSaida))
        print('Data de Entrega: {}'.format(self.dataEntrega))
        print('Valor da Locacao: {}'.format(self.valorLocacao))
        print('Documento do Cliente: {}'.format(self.cpfCliente))
        print('Status da locação: {}'.format(self.status))
        print('---------------------------------------')