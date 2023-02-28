from bytebank import Funcionario


def teste_idade():
    funcionario_teste = Funcionario('Lucas Carvalho', '13/03/2000', 1000)
    print(f'Teste = {funcionario_teste.idade()}')

teste_idade()