class Cpf:

    def __init__(self, documento):
        self._cpf = self.valida_cpf(documento)

    def __str__(self):
        return self.formata_cpf()

    def valida_cpf(self, documento):
        if len(str(documento)) == 11:
            return documento
        else:
            raise ValueError('CPF inválido')
        
    def formata_cpf(self):
        cpf_str = str(self._cpf)
        cpf_str1 = cpf_str[0:3]
        cpf_str2 = cpf_str[3:6]
        cpf_str3 = cpf_str[6:9]
        cpf_str4 = cpf_str[9:11]
        return '{}.{}.{}-{}'.format(cpf_str1, cpf_str2, cpf_str3, cpf_str4)