from config import *
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

print("hello my friend")

@dp.message_handler(commands = ['start'])
async def start(msg:types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Открыть веб-страницу', web_app=WebAppInfo(url='https://devabacus.github.io/telegram_bots_test/')))
    await msg.answer("Привет пацанчик", reply_markup=markup)
    
executor.start_polling(dp)

