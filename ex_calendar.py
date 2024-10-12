import calendar

month, day, year = map(int, input().split())

# Obtem em numero inteiro, o dia da semana especifico. 0=Segunda e 6=Domingo
date = calendar.weekday(year, month, day)

# O método 'day_name' retorna uma lista com os nomes de cada dai
# Com isso, a variavel 'name_day' vai acessar o dia da semana no indice 'date'
name_day = calendar.day_name[date]

print(name_day.upper())
"""
sample input

08 05 2015

sample output
WEDNESDAY
"""