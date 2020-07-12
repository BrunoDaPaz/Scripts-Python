from src.EnumStatus import EnumStatus

#classe Veiculo
class Veiculo:

    #cosntrutor da classe
    def __init__(self, nome, tipo, placa, marca, cor, status):
        self._nome = nome
        self._tipo = tipo
        self._placa = placa
        self._marca = marca
        self._cor = cor
        self._status = EnumStatus(status)

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def tipo(self):
        return self._tipo
    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def placa(self):
        return self._placa
    @placa.setter
    def placa(self, placa):
        self._placa = placa

    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def cor(self):
        return self._cor
    @cor.setter
    def cor(self, cor):
        self._cor = cor

    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, status):
        self._status = status

    #método que valida o status do veículo, se foi vendido ou não
    def validaStatus(self, status):
        if (EnumStatus.Disponível == status):
            print('Veículo disponível')
        elif (EnumStatus.Vendido == status):
            print('Veículo vendido')