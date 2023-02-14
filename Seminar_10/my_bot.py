#API token = 6002351552:AAGccH-dzaHfWV1jgG2yF2QKN4G71x7bISc

from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = '6002351552:AAGccH-dzaHfWV1jgG2yF2QKN4G71x7bISc'


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.Message):
    await msg.reply_to_message(f'Я бот. Приятно познакомиться',{msg.from_user.first_name})


@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
   if msg.text.lower() == 'привет':
       await msg.answer('Привет!')
   else:
       await msg.answer('У тебя отличное настроение!)!')


if __name__ == '__main__':
   executor.start_polling(dp)

