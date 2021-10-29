import datetime

first_date = datetime.date(2020, 12, 16)
second_date = datetime.date(2015, 12, 16)

result = first_date < second_date
print(result)


import datetime

# Data final
d2 = datetime.strptime('2017-05-05', '%Y-%m-%d')

# Data inicial
d1 = datetime.strptime('2017-05-01', '%Y-%m-%d')


# Calculo da quantidade de dias
quantidade_dias = abs((d2 - d1).days)
print(quantidade_dias)
