# Еще немного о друзьях
friends = {}
count = int(input("Введите количество друзей: "))
ages = 0
len_name = 0
max_name = " "
for i in range(count):
    name = input("Введите имя друга: ")
    if len_name < len(name):
        len_name = len(name)
        max_name = name
    age = int(input("Введите возраст друга: "))
    friends[name] = age
    ages = ages + age

print(friends)
average_age = ages/count
print("Средний возраст: ", int(average_age))
print("Самое длинное имя: ", max_name)