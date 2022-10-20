# Задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 60 -> 2, 2, 3, 5

import math
number = int(input('Введите число N: '))

def Factor(n):
    list = []
    for i in range(2, int(math.sqrt(n))+1):
        while n % i == 0:
            list.append(i)
            n //= i
        i += 1
    if n > 1:
        list.append(n)
    return list

print(f'Список простых множителей числа {number}: {Factor(number)}')
