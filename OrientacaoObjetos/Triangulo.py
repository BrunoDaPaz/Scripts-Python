class Triangulo:

    def __init__(self, ladoA, ladoB, ladoC):
        self._LadoA = ladoA
        self._LadoB = ladoB
        self._LadoC = ladoC

    @property
    def ladoA(self):
        return self._LadoA
    @ladoA.setter
    def ladoA(self, ladoA):
        self._LadoA = ladoA

    @property
    def ladoB(self):
        return self._LadoB
    @ladoB.setter
    def ladoB(self, ladoB):
        self._LadoB = ladoB

    @property
    def ladoC(self):
        return self._LadoC
    @ladoC.setter
    def ladoC(self, ladoC):
        self._LadoC = ladoC

    def calcularPerimetro(self, ladoA, ladoB, ladoC):
        perimetro = ladoA + ladoB + ladoC
        print('\nO perímetro do triângulo é {}'.format(perimetro))

    def getMaiorlado(self):
        if(self._LadoA > self._LadoB and self._LadoA > self._LadoC):
            print('\nO lado A do triângulo é o maior!')
        elif (self._LadoB > self._LadoA and self._LadoB > self._LadoC):
            print('\nO lado B do triângulo é o maior!')
        else:
            print('\nO lado C do triângulo é o maior!')