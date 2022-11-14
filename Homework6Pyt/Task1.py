# Задача 1. Дано натуральное число N. Найдите значение выражения:
# N + NN + NNN
# N может быть любой длины.
# N = 132:
# 132 + 132132 + 132132132 = 132264396
n = input('Введите число N: ')
def string(symbol, count): 
     return symbol * count  
n2=string(n,2)
n3=string(n,3)
sum = int(n) + int(n2) + int(n3)
print(f'N + NN + NNN = {sum}')