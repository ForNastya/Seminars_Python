# Реализуйте алгоритм перемешивания списка.
import random
list = [1, 7, 4, 2, 1]
print ('Оригинальный список: ' + str(list))
random.shuffle(list)
print ('Перемешанный список: ' + str(list))