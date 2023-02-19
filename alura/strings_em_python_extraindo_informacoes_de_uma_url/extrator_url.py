import re


class ExtratorURL:
    def __init__(self, url):
        self._url = self.sanitiza_url(url)
        self.valida_url()

    def __len__(self):
        return len(self._url)
    
    def __str__(self):
        return 'URL: ' + self._url + '\n' +\
        'Base: ' + self.get_url_base() + '\n' +\
        'Parâmetros: ' + self.get_url_parametros()

    def __eq__(self, other):
        return self._url == other._url

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''
    
    def valida_url(self):
        if not self._url:
            raise ValueError('A URL está vazia')
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        if not padrao_url.match(self._url):
            raise ValueError('A URL não é válida')
        
    def get_url_base(self):
        indice_interrogacao = self._url.find('?')
        return self._url[:indice_interrogacao]
    
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