import re
import requests


class BuscaEndereco:

    def __init__(self, cep):
        cep = str(cep)
        if self.valida_cep(cep):
            self.__cep = cep
        else:
            raise ValueError('CEP inválido')
        self.retorna_dados()

    def __str__(self):
        return (
f'''{self.logradouro}{', ' if len(self.complemento) > 0 else ''}{self.complemento}
{self.bairro}
{self.cep}. {self.localidade}/{self.uf}'''
        )
    
    @property
    def cep(self):
        return self.formata_cep()
    
    @property
    def logradouro(self):
        return self.__dados.get('logradouro')

    @property
    def complemento(self):
        return self.__dados.get('complemento')
    
    @property
    def bairro(self):
        return self.__dados.get('bairro')
    
    @property
    def localidade(self):
        return self.__dados.get('localidade')
    
    @property
    def uf(self):
        return self.__dados.get('uf')
    
    @property
    def ibge(self):
        return self.__dados.get('ibge')
    
    @property
    def gia(self):
        return self.__dados.get('gia')
    
    @property
    def ddd(self):
        return self.__dados.get('ddd')
    
    @property
    def siafi(self):
        return self.__dados.get('siafi')

    @property
    def dados(self):
        return self.__dados

    def valida_cep(self, cep):
        padrao = '([0-9]{5})-?([0-9]{3})'
        if re.search(padrao, cep) is not None:
            return True
        else:
            return False
        
    def formata_cep(self):
        padrao = '([0-9]{5})-?([0-9]{3})'
        cep = re.search(padrao, self.__cep)
        return '{}-{}'.format(cep.group(1), cep.group(2))

    def retorna_dados(self):
        url = 'https://viacep.com.br/ws/{}/json'.format(self.__cep)
        r = requests.get(url)
        self.__dados = r.json()