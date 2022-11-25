#Задача 3. В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год. 
# Каждому месяцу соответствует своя строка. 
# Определите самый жаркий и самый холодный 7-дневный промежуток этого периода. Выведите его даты.
import random
from datetime import datetime, timedelta

temperature = [0] * 5
value = []
value_sum = 0
weekly_maximum = 0
weekly_minimum = 1000
may = 0
june = 1
jule = 2
august = 3
september = 4
temperature[may] = list(random.randint(6, 18) for i in range(31))
temperature[june] = list(random.randint(11, 23) for i in range(30))
temperature[jule] = list(random.randint(14, 24) for i in range(31))
temperature[august] = list(random.randint(11, 21) for i in range(31))
temperature[september] = list(random.randint(6, 15) for i in range(30))
for row in temperature:
    print(row)
for i in range(len(temperature)):
    for j in range(len(temperature[i])):
        value.append(temperature[i][j])
for i in range(len(value) - 6):
    value_sum = 0
    value_sum = value[i] + value[i+1] + value[i+2] + value[i+3] + value[i+4] + value[i+5] + value[i+6]
    if value_sum > weekly_maximum:
        weekly_maximum = i
    elif value_sum < weekly_minimum:
        weekly_minimum = i
start_data = '2022-05-01' 
dt = datetime.strptime(start_data, '%Y-%m-%d')
result_start_max_day = (dt + timedelta(days=weekly_maximum)).strftime('%Y-%m-%d')
result_finish_max_day = (dt + timedelta(days=weekly_maximum+7)).strftime('%Y-%m-%d')
result_start_min_day = (dt + timedelta(days=weekly_minimum)).strftime('%Y-%m-%d')
result_finish_min_day = (dt + timedelta(days=weekly_minimum+7)).strftime('%Y-%m-%d')
print(f"Самая теплая неделя с {result_start_max_day} по {result_finish_max_day}")
print(f"Самая холодная неделя с {result_start_min_day} по {result_finish_min_day}")

