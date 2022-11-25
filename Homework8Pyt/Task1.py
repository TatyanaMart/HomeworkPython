# Задача 1. В каждой группе учится от 20 до 30 студентов. По итогам экзамена все оценки заносятся в таблицу. 
# Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом.

import random


def fillArray():
    count_group = random.randint(2, 10)
    print(f"Количество групп: {count_group}")
    students_list = [0] * count_group
    for i in range(count_group):
        count_students = random.randint(20, 30)
        print(f"Количество студентов в {i + 1} группе: {count_students}")
        students_list[i] = list(0 for j in range(count_students))
        for k in range(count_students):
            students_list[i][k] = random.randint(2, 5)
    return students_list


new_list = fillArray()
list_gpa = []
for i in new_list:
    list_int = map(int, i)
    summa = sum(list_int)
    list_gpa.append(round(summa / len(i), 2))
print("Таблица с оценками:")
for i in new_list:
    print(i)
print(f"Средние баллы по группам: {list_gpa}")
print(f"Лучший средний балл в {list_gpa.index(max(list_gpa)) + 1} группе")