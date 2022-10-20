# Задача 1. Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8

n = int(input('Введите кол-во элементов Фибоначчи: '))
print(f'Последовательность Фибоначчи для первых {n} элементов записалась в файл fibonachi.txt')

def fib(n): 
    if n in [1, 2]: 
        return 1
    else:
        return fib(n-1) + fib(n-2)

list = []
for e in range(1, n+1):
    list.append(fib(e))

data = open('fibonachi.txt', 'w')
data.writelines(str(list))
data.close() 
