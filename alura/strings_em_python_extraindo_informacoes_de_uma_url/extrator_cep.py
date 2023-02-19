endereco = 'Avenida Ary Carneiro, 419, Vila Maria - Itanhandu (MG) - 37646-000'

import re

padrao = re.compile('[0-9]{5}[-]?[0-9]{3}')
busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)