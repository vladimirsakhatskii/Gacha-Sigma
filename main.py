from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import app.database
import os

load_dotenv()
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)

app.create_table()

admins = [
    '5593392332',
]

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await bot.send_message(
        text=f'{message.from_user.first_name}, добро пожаловать!',
        chat_id=message.from_user.id)
    msg = app.database.add_user(message.chat.id)
    await message.answer(text='Желаю тебе удачи на просторах этой гачи)' + msg)

@dp.message_handler(commands=['cod'])
async def cod(message: types.Message):
    app.database.add_transaction(message.chat.id)
    await message.answer(text='Код')

@dp.message_handler(commands=['play'])
async def play(message: types.Message):
    await message.answer(text = 'Игра')
    
if __name__ == '__main__':
    print('Bot started!')
    executor.start_polling(dp)
