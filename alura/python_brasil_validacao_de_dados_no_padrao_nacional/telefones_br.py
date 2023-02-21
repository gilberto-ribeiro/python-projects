import re


class TelefoneBR:

    def __init__(self, numero):
        numero = str(numero)
        if self.valida(numero):
            self.__numero = numero
        else:
            raise ValueError('Número de telefone inválido')
    
    def __str__(self):
        return self.formata()

    def valida(self, numero):
        padrao = '[0-9]{2}[0-9]{4,5}[0-9]{4}'
        if re.search(padrao, numero) is None:
            return False
        else:
            return True
        
    def formata(self):
        ddd = self.__numero[:2]
        grupo2 = self.__numero[-4:]
        grupo1 = self.__numero.removeprefix(ddd).removesuffix(grupo2)
        return '({}) {}-{}'.format(ddd, grupo1, grupo2)
