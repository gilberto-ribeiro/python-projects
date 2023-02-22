from fabrica_fila import FabricaFila


fila_teste = FabricaFila.pega_fila('prioritaria')

fila_teste.atualiza_fila()
print(fila_teste.fila)
fila_teste.atualiza_fila()
print(fila_teste.fila)
fila_teste.atualiza_fila()
print(fila_teste.fila)
fila_teste.atualiza_fila()
print(fila_teste.fila)
print(fila_teste.chama_cliente(15))
print(fila_teste.fila)
print(fila_teste.chama_cliente(15))
print(fila_teste.fila)
fila_teste.atualiza_fila()
print(fila_teste.fila)
fila_teste.atualiza_fila()
print(fila_teste.fila)
print(fila_teste.chama_cliente(15))
print(fila_teste.fila)
print(fila_teste.estatistica('22/02/2023', 152, 'detail'))
