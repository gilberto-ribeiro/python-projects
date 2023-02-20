from cpf_cnpj import CpfCnpj
from validate_docbr import CNPJ

doc = CpfCnpj('51423928000110', 'cnpj')
print(doc)
print(doc.tipo_documento)