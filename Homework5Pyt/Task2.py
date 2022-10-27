# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа, описывающие случайную возрастающую последовательность.
# Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
import random
numbers = [1, 5, 2, 3, 4, 6, 1, 7]
#numbers = [random.randint(1, 10) for i in range(8)]
print(numbers)

list = [numbers[0]]
for i in numbers:
    if i > list[-1]:
        list.append(i)
print(list)
