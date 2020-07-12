class Retangulo:

    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2

    def get_lado1(self):
        return self.lado1
    def get_lado2(self):
        return self.lado2
    def set_lado1(self, lado1):
        self.lado1 = lado1
    def set_lado2(self, lado2):
        self.lado2 = lado2

    def calcularArea(self, paramLado1, paramLado2):
        self.area = (paramLado1*paramLado2)

    def calcularPerimetro(self, paramLado1, paramLado2):
        self.perimetro = (2*paramLado1) + (2*paramLado2)

