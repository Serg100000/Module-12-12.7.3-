money = int(input('Введите сумму вклада: '))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

ТКБ = int((per_cent['ТКБ'])*(money/100))
СКБ = int((per_cent['СКБ'])*(money/100))
ВТБ = int((per_cent['ВТБ'])*(money/100))
СБЕР = int((per_cent['СБЕР'])*(money/100))

deposit = [ТКБ, СКБ, ВТБ, СБЕР]
print(deposit)

d = {'TKB': 5.6, 'SKB': 5.9, 'VTB': 4.28, 'SBER': 4.0}
max_val = max(d.values())
print(max_val)

i = int((max_val)*(money/100))
print(i)