class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print(f'Criando o objeto: {self}')
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite