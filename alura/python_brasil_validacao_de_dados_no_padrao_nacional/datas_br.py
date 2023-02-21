from datetime import datetime, timedelta


class DataBR:

    def __init__(self):
        self.__momento_cadastro = datetime.now()

    def __str__(self):
        return self.formata_data()

    @property
    def dia(self):
        return self.__momento_cadastro.day
    
    @property
    def dia_da_semana(self):
        dias_da_semana = [
            'segunda-feira', 'terça-feira', 'quarta-feira',
            'quinta-feira', 'sexta-feira', 'sábado', 'domingo'
        ]
        # dias_da_semana = [wd + '-feira' if i in range(5) else wd for i, wd in enumerate(dias_da_semana)]
        return dias_da_semana[self.__momento_cadastro.weekday()]
    
    @property
    def mes(self):
        meses = [
            'janeiro', 'fevereiro', 'março', 'abril',
            'maio', 'junho', 'julho', 'agosto',
            'setembro', 'outubro', 'novembro', 'dezembro'
        ]
        return meses[self.__momento_cadastro.month - 1]

    @property
    def ano(self):
        return self.__momento_cadastro.year
    
    def formata_data(self):
        return self.__momento_cadastro.strftime('%d/%m/%Y %H:%M')
    
    def tempo_cadastro(self):
        return datetime.now() - self.__momento_cadastro