# Задача 2. В первой строке файла находится информация об ассортименте мороженого, во второй - информация о том, какое мороженое 
# есть на складе. Выведите названия того товара, который закончился.
# 1. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2. «Сливочное», «Вафелька», «Сладкоежка»
# Закончилось: «Бурёнка»
with open('IceCream.txt', 'r', encoding='utf-8') as ice:
    assortment = set(ice.readline().rstrip().split(', '))
    stock = set(ice.readline().rstrip().split(', '))
    print(f'Закончилось:', *assortment - stock)