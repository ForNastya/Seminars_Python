# Старший и младший
friends = {}
count = int(input('Введите количество друзей: '))
for i in range(count):
    name = input('Введите имя друга: ')
    age = int(input('Введите возраст друга: '))
    friends[name] = age
print(friends)

min_age = min(friends.values())
for name, am in friends.items():
    if am == min_age:
        print(name)