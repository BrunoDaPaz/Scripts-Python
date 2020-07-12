from src.Fatura import Fatura

if __name__ == '__main__':
    #construtor criando fatura
    faturaPositiva = Fatura(1, 'vinho', 5, 75.0)
    faturaNegativa = Fatura(2, 'refrigerante', 10, -3.90)

    #método com valor negativo
    faturaNegativa.comprarItem(faturaNegativa.quantidade_comprada, faturaNegativa.preco_unitario)

    #método com valor positivo
    faturaPositiva.comprarItem(faturaPositiva.quantidade_comprada, faturaPositiva.preco_unitario)

    #método imprimeDetalhes
    faturaPositiva.imprimeDetalhes(faturaPositiva.numero_item_faturado, faturaPositiva.descricao_item, faturaPositiva.quantidade_comprada, faturaPositiva.preco_unitario)

    #chamando o método getValorFaturado
    faturaPositiva.getValorFaturado(faturaPositiva.quantidade_comprada, faturaPositiva.preco_unitario)