from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = '6138206893:AAHN7A7AIYgzAJJlwvJYYgqlYuRgjjPdvtE'


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def greetings (message: types.Message):
   await message.reply('Привет!\nЯ Эхо-бот от Anastasiya!\nОтправь мне любое сообщение, и я тебе обязательно отвечу.')


@dp.message_handler()
async def echo(message: types.Message):
   await message.answer(message.text)

