# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.
print('x | y | z | ¬ X v Y')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            print(f'{x} | {y} | {z} | {int(not(x and y) or z)}')
