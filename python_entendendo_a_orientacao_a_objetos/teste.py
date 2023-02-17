def criar_conta(numero, titular, saldo, limite):
    conta = {'numero': numero, 'titular': titular, 'saldo': saldo, 'limite': limite}
    return conta


def sacar(conta, valor):
    if conta['saldo'] < valor:
        print('Saldo insuficiente')
    else:
        conta['saldo'] -= valor


def depositar(conta, valor):
    conta['saldo'] += valor


def extrato(conta):
    print('Seu saldo atual é de {}.'.format(conta['saldo']))
