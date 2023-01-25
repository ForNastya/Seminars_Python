# Фрукты.
fruits = {}
count = int(input('Введите сколько фруктов: '))
for i in range(count):
    name = input('Введите название фрукта: ')
    fruitcount = int(input('Введите количество: '))
    fruits[name] = fruitcount
print(fruits)