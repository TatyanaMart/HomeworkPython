# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2
line1 = input('Введите слово: ')
line2 = input('Введите предложение: ')

if len(line1) <= len(line2):
    for i in range(len(line1)):
        count = 0
        for j in range(len(line2)):
            if line1[i] == line2[j]:
                count += 1
        print(line1[i], '-', count)
else:
    print('Ошибка: длина слова превышает длину предложения')
