# Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке. 
# Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают Список уникальных элементов [1, 4, 2, 3, 6, 7]
import random
numbers = [random.randint(1, 10) for i in range(8)]
print(numbers)
count = 0
for i in numbers:
    if numbers.count(i) > 1:
        count +=1

print("Кол-во повторяющихся элементов: ", count)
print("Список уникальных элементов: ", list(set(numbers)))
