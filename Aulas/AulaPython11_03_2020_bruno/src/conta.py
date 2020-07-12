class Conta:
        def __init__(self, numero, titular, saldo, limite=1000.0):
            self.numero = numero
            self.titular = titular
            self.saldo = saldo
            self.limite = limite

if __name__ == '__main__':
     conta = Conta('123-4','joão',1200.0, 1000.0)
     print(conta.titular)