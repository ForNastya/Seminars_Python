# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
a = input('Введите число')
sum = 0
for number in a:
    if number != '.':
        sum += int(number)
print(sum)