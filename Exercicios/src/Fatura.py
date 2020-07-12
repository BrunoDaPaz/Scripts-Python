class Fatura:

    def __init__(self, numero_item_faturado, descricao_item, quantidade_comprada, preco_unitario):
        self.numero_item_faturado = numero_item_faturado
        self.descricao_item = descricao_item
        self.quantidade_comprada = quantidade_comprada
        self.preco_unitario = preco_unitario

    def get_numero_item_faturado(self):
        return self.numero_item_faturado
    def get_descricao_item(self):
        return self.descricao_item
    def get_quantidade_comprada(self):
        return self.quantidade_comprada
    def get_preco_unitario(self):
        return self.preco_unitario

    def set_numero_item_faturado(self, numero_item_faturado):
        self.numero_item_faturado = numero_item_faturado
    def set_descricao_item(self, descricao_item):
        self.descricao_item = descricao_item
    def set_quantidade_comprada(self, quantidade_comprada):
        self.quantidade_comprada = quantidade_comprada
    def set_preco_unitario(self, preco_unitario):
        self.preco_unitario = preco_unitario

    def comprarItem(self, paramQuantidade_comprada, paramPreco_unitario):
        if (paramQuantidade_comprada <= 0):
            self.quantidade_comprada = 0
        elif (paramPreco_unitario <= 0):
           self.preco_unitario = 0.0
           print('O valor unitário deve ser maior que 0')

    def imprimeDetalhes(self, paramNumero_item_faturado, paramDescricao_item, paramQuantidade_comprada, paramPreco_unitario):
        print('\n' + 'Código do item: ' + str(int(paramNumero_item_faturado)))
        print('Descrição do item: ' + str(paramDescricao_item))
        print('Quantidade do item: ' + str(int(paramQuantidade_comprada)))
        print('Valor do item: ' + 'R$' + str(float(paramPreco_unitario)))

    def getValorFaturado(self, paramQuantidade_comprada, paramPreco_unitario):
        valorFaturado = paramPreco_unitario * paramQuantidade_comprada
        print('O Valor total da Fatura é: ' + 'R$' + str(float(valorFaturado)))
