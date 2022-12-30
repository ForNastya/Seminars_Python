# Напишите программу, которая найдёт произведение пар чисел списка.
numbers = [9, 1, 4, 7, 10, 15]
print ('Оригинальный список:' + str(numbers))
res = []
for el in range (0, len(numbers), 2):
    res.append(numbers[el] * numbers[el + 1])
print ('Произведение пар чисел: ' + str(res))

