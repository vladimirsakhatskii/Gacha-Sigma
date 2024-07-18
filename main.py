from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import BotCommand
from dotenv import load_dotenv
import os
# from app import Admin os Admin

load_dotenv()
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)

bot_commands = [
        BotCommand(command="/start", description="Запустить бота"),
        BotCommand(command="/play", description="Начать игру"),
        BotCommand(command="/cod", description="Отправить код")
    ]

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    # if message.from_user.id == os.getenv('ADMIN_ID[3]' or message.from_user.id == os.getenv('ADMIN_ID[1]' or message.from_user.id == os.getenv('ADMIN_ID[2]'):
    await bot.send_message(
        text=f'{message.from_user.first_name}, добро пожаловать!',
        chat_id=message.from_user.id)
    await message.answer(text='Желаю тебе удачи на просторах этой гачи)')
    await bot.set_my_commands(bot_commands)

@dp.message_handler(commands=['cod'])
async def cod(message: types.Message):
    await message.answer(text='Код')

@dp.message_handler(commands=['play'])
async def play(message: types.Message):
    await message.answer(text = 'Игра')

if __name__ == '__main__':
    print('Bot is running!')
    executor.start_polling(dp, skip_updates=True)