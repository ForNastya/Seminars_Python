# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
list = []
numbers = [1, 9, 22, 5, 22, 7, 1]
for _ in numbers:
    if numbers.count(_) == 1:
        list += [_]
print(list)
