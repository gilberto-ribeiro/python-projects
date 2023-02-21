import re


class TelefoneBR:

    def __init__(self, numero):
        numero = str(numero)
        if self.valida_numero(numero):
            self.__numero = numero
        else:
            raise ValueError('Número de telefone inválido')
    
    def __str__(self):
        return self.formata_numero()

    def valida_numero(self, numero):
        padrao = '([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        if re.search(padrao, numero) is None:
            return False
        else:
            return True
        
    def formata_numero(self):
        padrao = '([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})'
        numero = re.search(padrao, self.__numero)
        ddi = numero.group(1) if numero.group(1) is not None else '55'
        ddd = numero.group(2)
        grupo1 = numero.group(3)
        grupo2 = numero.group(4)
        return '+{} {} {}-{}'.format(ddi, ddd, grupo1, grupo2)
