# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

with open('text.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Введите текст: '))
with open('text.txt', 'r') as file:
    my_txt = file.readline()
    txt_chan = my_txt.split()

print(my_txt)

def file_encod(txt):
    encond = ''
    prev_char = ''
    count = 1
    if not txt:
        return ''

    for char in txt:
        if char != prev_char:
            if prev_char:
                encond += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encond += str(count) + prev_char
        return encond


txt_chan = file_encod(my_txt)

with open('text_write.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{txt_chan}')
print(txt_chan)