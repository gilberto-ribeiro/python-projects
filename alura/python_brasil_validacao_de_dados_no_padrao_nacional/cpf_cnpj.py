from validate_docbr import CPF, CNPJ


class CpfCnpj:

    def __init__(self, documento, tipo_documento='CPF'):
        self.__tipo_documento = tipo_documento.upper()
        documento = str(documento)
        self.instancia_documento(documento)

    def __str__(self):
        if self.__tipo_documento == 'CPF':
            return self.formata_cpf()
        elif self.__tipo_documento == 'CNPJ':
            return self.formata_cnpj()

    def instancia_documento(self, documento):
        if self.__tipo_documento == 'CPF':
            if self.valida_cpf(documento):
                self._cpf = documento
            else:
                raise ValueError('CPF inválido')
        elif self.__tipo_documento == 'CNPJ':
            if self.valida_cnpj(documento):
                self._cnpj = documento
            else:
                raise ValueError('CNPJ inválido')
        else:
            raise ValueError('Tipo de documento inválido')

    @property
    def tipo_documento(self):
        return self.__tipo_documento

    def valida_cpf(self, documento):
        if len(documento) == 11:
            cpf = CPF()
            return cpf.validate(documento)
        else:
            raise ValueError('Quantidade de dígitos inválida')

    def valida_cnpj(self, documento):
        if len(documento) == 14:
            cnpj = CNPJ()
            return cnpj.validate(documento)
        else:
            raise ValueError('Quantidade de dígitos inválida')
        
    def formata_cpf(self):
        cpf = CPF()
        return cpf.mask(self._cpf)
    
    def formata_cnpj(self):
        cnpj = CNPJ()
        return cnpj.mask(self._cnpj)