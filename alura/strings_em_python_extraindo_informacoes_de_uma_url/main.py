# url = 'https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'
url = ' \n '

# Código feito por mim antes de assistir às aulas
# url_base, url_parameters = url.split('?')
# parameters = url_parameters.split('&')
# parameters_dict = dict([tuple(parameter.split('=')) for parameter in parameters])

# Sanitização da URL
# url = url.replace(' ', '')
url = url.strip()

#
if url == '':
    raise ValueError('A URL está vazia')

#Separa base e parametros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]

# Busca o valor de um parâmetro
parametro = 'quantidade'
indice_parametro = url_parametros.find(parametro)
indice_valor = indice_parametro + len(parametro) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)
