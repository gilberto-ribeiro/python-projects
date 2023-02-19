# Código feito por mim antes de assistir às aulas
# url_base, url_parameters = url.split('?')
# parameters = url_parameters.split('&')
# parameters_dict = dict([tuple(parameter.split('=')) for parameter in parameters])

class ExtratorURL:
    def __init__(self, url):
        self._url = self.sanitiza_url(url)
        self.valida_url()
        self.valida_base()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''
    
    def valida_url(self):
        if not self._url:
            raise ValueError('A URL está vazia')
        
    def get_url_base(self):
        indice_interrogacao = self._url.find('?')
        return self._url[:indice_interrogacao]

    def valida_base(self):
        if not self.get_url_base().startswith('https'):
            raise ValueError('A URL não inicia com https')
        if not self.get_url_base().endswith('/cambio'):
            raise ValueError('Base da URL não possui cambio')
    
    def get_url_parametros(self):
        indice_interrogacao = self._url.find('?')
        return self._url[indice_interrogacao+1:]
    
    def get_valor_parametro(self, parametro):
        indice_parametro = self.get_url_parametros().find(parametro)
        indice_valor = indice_parametro + len(parametro) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

url = 'https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'

extrator_url = ExtratorURL(url)
valor_quantidade = extrator_url.get_valor_parametro('quantidade')
print(valor_quantidade)