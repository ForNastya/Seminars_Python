# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def del_w(f):
    return False if 'абв' in f else True

print('Введите текст: ')
a = input()

a = a.split()
print(a)
a = list(filter(del_w,a))
print(a)
