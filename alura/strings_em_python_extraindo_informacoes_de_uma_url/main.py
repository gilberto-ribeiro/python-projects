from extrator_url import ExtratorURL


def converter_moeda(url, imprime=False):
    extrator_url = ExtratorURL(url)
    fcrd = 5.50
    moedas = ('real', 'dolar')
    matriz_conversao = [[1, 1 / fcrd], [fcrd, 1]]
    moeda_origem = extrator_url.get_valor_parametro('moedaOrigem')
    moeda_destino = extrator_url.get_valor_parametro('moedaDestino')
    quantidade = float(extrator_url.get_valor_parametro('quantidade'))
    indice_origem = moedas.index(moeda_origem)
    indice_destino = moedas.index(moeda_destino)
    quantidade_convertida = quantidade * matriz_conversao[indice_origem][indice_destino]
    if imprime:
        print(f'{quantidade} {moeda_origem} é igual a {quantidade_convertida} {moeda_destino}.')
    else:
        return quantidade_convertida


url = 'https://www.bytebank.com/cambio?moedaOrigem=dolar&moedaDestino=real&quantidade=100'

converter_moeda(url, True)