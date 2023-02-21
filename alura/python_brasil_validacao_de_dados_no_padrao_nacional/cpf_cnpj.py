# Refatorar futuramente, usando herança em classes e métodos de classe.


from validate_docbr import CPF, CNPJ


class Documento:

    @staticmethod
    def cria_documento(documento):
        documento = str(documento)
        if len(documento) == 11:
            return DocCPF(documento)
        elif len(documento) == 14:
            return DocCNPJ(documento)
        else:
            raise ValueError('Quantidade de dígitos inválida')


class DocCPF:

    def __init__(self, documento):
        if self.valida(documento):
            self.__cpf = documento
        else:
            raise ValueError('CPF inválido')

    def __str__(self):
        return self.formata()

    @property
    def tipo(self):
        return 'CPF'

    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)
    
    def formata(self):
        mascara = CPF()
        return mascara.mask(self.__cpf)
    

class DocCNPJ:

    def __init__(self, documento):
        if self.valida(documento):
            self.__cnpj = documento
        else:
            raise ValueError('CNPJ inválido')

    def __str__(self):
        return self.formata()

    @property
    def tipo(self):
        return 'CNPJ'

    def valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)
    
    def formata(self):
        mascara = CNPJ()
        return mascara.mask(self.__cnpj)