class Filme:

    def __init__(self, titulo_filme, resumo_filme, duracao):
        self.titulo_filme = titulo_filme
        self.resumo_filme = resumo_filme
        self.duracao = duracao

    def get_titulo_filme(self):
        return self.titulo_filme
    def get_resumo_filme(self):
        return self.resumo_filme
    def get_duracao(self):
        return self.duracao

    def set_titulo_filme(self, titulo_filme):
        self.titulo_filme = titulo_filme
    def set_resumo_filme(self, resumo_filme):
        self.resumo_filme = resumo_filme
    def set_duracao(self, duracao):
        self.duracao = duracao

    def mostrarFilme(self, paramTitulo_filme, paramResumo_filme):
        print(paramTitulo_filme + ' - ' + paramResumo_filme)

    def horaMinuto(self, paramDuracao):
        horas = int(paramDuracao / 60)
        minutos = (paramDuracao - (horas * 60))
        print('{}:{}'.format(horas, minutos))