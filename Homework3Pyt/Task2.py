# Задача 2. В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.

letter = input('Введите первую букву названия фрукта (заглавную): ')
with open('MyFruits.txt', encoding='utf-8') as data:
    fruits = data.readlines()
    for fructik in fruits:
        if fructik[0] == letter:
            print(fructik)
