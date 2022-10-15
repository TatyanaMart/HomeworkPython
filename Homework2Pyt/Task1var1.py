# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# 1 вариант
n = int(input('Введите число: '))


def Factorial(n):
    if n == 1:
        return 1
    else:
        return n * Factorial(n-1)


list = []
for i in range(1, n+1):
    list.append(Factorial(i))
print(list)
