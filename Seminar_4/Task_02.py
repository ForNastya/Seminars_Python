# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
number = int(input('Введите число: '))
for _ in range (1, number + 1):
    if(number % _ == 0):
        print(_)
        
