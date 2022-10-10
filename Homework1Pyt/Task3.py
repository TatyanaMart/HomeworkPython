# Задача 3. Напишите программу, которая по заданному номеру четверти, показывает диапазон
# возможных координат точек в этой четверти (x и y). 1 -> x > 0, y > 0
quarter = ["Х>0, Y>0", "Х<0, Y>0", "Х<0, Y<0", "Х>0, Y<0"]
number = int(input('Введите номер четверти: '))
if number < 1 or number > 4:
    print("Ошибка! Четверть не существует")
else:
    print(f"Диапазон координат {number} четверти: {quarter[number-1]}")