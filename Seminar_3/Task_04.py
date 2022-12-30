# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
number_a = int(input('Введите число: '))
number_b = ''
while number_a > 0:
    number_b = str(number_a % 2) + number_b
    number_a = number_a // 2
print(number_b)
