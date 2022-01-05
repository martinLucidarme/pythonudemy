# https:// docs.python.org/3.0/library/datetime
# datetime(ano, mes, dia, hora, minuto, segundo)


"""
usado para salvar as data no sistema
"""

from datetime import datetime, timedelta
from locale import setlocale, LC_ALL

data = datetime(2019, 4, 20, 10, 53, 20)
print(data)
print(data.strftime('%d/%m/%Y %H:%M:%S'))  # formata a data: ver doc > Directive

data2 = datetime.strptime('20/04/2019', '%d/%m/%Y')
# recebe data e formato, mais comum pq geralmente recebe data como string
print(data2)
print(data.timestamp())  # timestamp = contagem de segundos de 01-01-1970 ate data

data3 = datetime.fromtimestamp(1555768400.0)  # retorna data a partir do timestamp
print(data3)

data4 = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
data4 = data4 + timedelta(days=5, seconds=59 * 60)  # adiciona 5 dias e 59 minutos
print(data4.strftime('%d/%m/%Y %H:%M:%S'))

data5 = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
d5 = datetime.strptime('25/04/1987 22:33:00', '%d/%m/%Y %H:%M:%S')
dif = d5 - data5
print(dif)  # mostra a diferença de tempo entre as duas datas
print(dif.seconds)  # numero de segundos entre as horas
print(dif.total_seconds())  # numero de segundos totais de diferença
print(dif.days)

print(d5.time())  # mostra só as horas duma data

print(data5 < d5)  # pode comparar as datas

dt = datetime.now()  # pega a data atual
formatacao = dt.strftime('%A, %d de %B de %Y')
print(formatacao)  # vai aparecer em ingles

setlocale(LC_ALL, '')  # pega local padrão do computador (pode fazer: setlocale(LC_ALL, 'pt_BR.utf-8')
formatacao2 = dt.strftime('%A, %d de %B de %Y')
print(formatacao2)

