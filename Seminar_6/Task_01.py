#Создайте список из случайных чисел. Найдите количество различных элементов в нем.
import random

some_list = [random.randint(1,20) for i in range(20)]
print(some_list)
list = set(some_list)
print(len(list))