# Artigo: https://www.alura.com.br/artigos/lidando-com-datas-e-horarios-no-python

from datetime import date, datetime, timezone, timedelta

# FORMATAÇÃO DE DATA

data_atual = date.today()

# Formatação usando o método format()
# data_em_texto = '{:02d}/{:02d}/{:04d}'.format(data_atual.day, data_atual.month, data_atual.year)

# Formatação usando o método strftime()
data_em_texto = data_atual.strftime('%d/%m/%Y')

print(data_em_texto)

# FORMATAÇÃO DE DATA E HORA

data_e_hora_atuais = datetime.now()

data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')

print(data_e_hora_em_texto)

# FORMATACAO DE DATA E HORA COM FUSO-HORARIO

diferenca = timedelta(hours=-4)

fuso_horario = timezone(diferenca)

data_e_hora_atuais_amazonas = data_e_hora_atuais.astimezone(fuso_horario)

data_e_hora_amazonas_em_texto = data_e_hora_atuais_amazonas.strftime('%d/%m/%Y %H:%M')

print(data_e_hora_amazonas_em_texto)

# FALTA IMPLEMENTAR A BIBLIOTECA pytz