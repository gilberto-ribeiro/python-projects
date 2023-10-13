class Conta:

    numeros_dos_bancos = {
        'BB': '001',
        'Caixa': '104',
        'Bradesco': '237',
        'Itau': '341'
    }

    def __init__(self, numero, titular, saldo, limite = 1000):
        print(f'Criando o objeto: {self}')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'Saldo de {self.__saldo:.2f} do titular {self.__titular}.')

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print('Limite insuficiente.')

    def deposita(self, valor):
        self.__saldo += valor

    def transfere(self, outra_conta, valor):
        if valor >= 0:
            self.saca(valor)
            outra_conta.deposita(valor)
#             print(
# f'''Tranferência concluída com sucesso!

# Valor: R${valor:.2f}
# Conta de origem: {self.__numero}
# Conta de destino: {outra_conta.__numero}
# ''')

    def __pode_sacar(self, valor):
        return valor <= (self.__saldo + self.__limite)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @property
    def titular(self):
        return self.__titular

    @property
    def numero(self):
        return self.__numero
    
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def __numero_do_banco(banco):
        return Conta.numeros_dos_bancos[banco]

class Data:

    def __init__(self, dia, mes, ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    def formatada(self):
        print(f'{self.__dia}/{self.__mes}/{self.__ano}')