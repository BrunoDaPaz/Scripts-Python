from src.Enum.EnumStatus import EnumStatus

class Veiculo:

    def __init__(self, nome, tipo, placa, marca, cor, modelo, ano, rodas, status):
        self._nome = nome
        self._tipo = tipo
        self._placa = placa
        self._marca = marca
        self._cor = cor
        self._modelo = modelo
        self._ano = ano
        self._rodas = rodas
        self._status = EnumStatus(status)
        print('\n>Veiculo Criado<')

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
    def modelo(self):
        return self._modelo
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def ano(self):
        return self._ano
    @ano.setter
    def ano(self, ano):
        self._ano = ano

    @property
    def rodas(self):
        return self._rodas
    @rodas.setter
    def rodas(self, rodas):
        self._rodas = rodas

    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, status):
        self._status = status

    #método que valida o status do veículo, se foi vendido ou não
    def validaStatus(self, status):
        if (status == EnumStatus.Disponivel):
            print('VALIDAÇÃO: Veículo disponível')
            print('---------------------------------------')
        elif (status == EnumStatus.Vendido):
            print('VALIDAÇÃO: Veículo indisponvível')
            print('---------------------------------------')

    def validaAnoVeiculo(self, ano):
        if (ano >= 2010):
            print('VALIDAÇÃO: Ano do veículo válido para cadastro.')
            print('---------------------------------------')
            return True
        elif(ano < 2010):
            print('VALIDAÇÃO: Não é aceito o cadastro de veículos com data inferior à 2010.')
            print('---------------------------------------')
            return False

    def validaNumeroRodas(self, rodas):
        if(rodas < 4):
            print('VALIDAÇÃO: Veículo inválido considerado motocicleta, tricíclo ou motoneta.\nPara cadastro somente veículos com 4 rodas ou mais.')
            print('---------------------------------------')
            return False
        elif(rodas >= 4):
            print('VALIDAÇÃO: Número de rodas válido considerando o automóvel.')
            print('---------------------------------------')
            return True

    def inserir(self):
        print('---------------------------------------')
        print('Nome: {}'.format(self.nome))
        print('Tipo de veículo: {}'.format(self.tipo))
        print('Placa: {}'.format(self.placa))
        print('Marca: {}'.format(self.marca))
        print('Cor: {}'.format(self.cor))
        print('Modelo: {}'.format(self.modelo))
        print('Ano: {}'.format(self.ano))
        print('Número de rodas: {}'.format(self.rodas))
        print('Status: {}'.format(self.status))
        print('---------------------------------------')