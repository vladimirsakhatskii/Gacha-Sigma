from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

load_dotenv()
bot = Bot(os.getenv['TOKEN'])
dp = Dispatcher(bot=bot, storage=storage)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    print('Bot started!')
    
if __name__ == '__main__':
    executor.start_polling(dp)
