# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
numbers = [1.1, 1.2, 3.1, 5, 10.01]
a = []
for i in range(len(numbers)):
    if numbers[i] % 1 != 0:
        a.append(numbers[i])
res = [round(numbers[i] % 1, 2) for i in range(len(a))]
print(f"{res} = {max(res) - min(res)}")