import datetime

def logger(time):
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(f'время запроса: {str(datetime.datetime.now())} \n')

def logger(l_time):
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(f'время запроса: {str(datetime.datetime.now())} \n')