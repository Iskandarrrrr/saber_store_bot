from aiogram import Bot, Dispatcher, executor
from dotenv import load_dotenv
import os
from keyboards import *
from saber_pars import pars_saber
from aiogram.types import Message
from configs import get_value
import time

load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = Bot(TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def command_start(message: Message):
    await message.answer('Salom! Saber magaziniga hush kelibsiz!')
    await show_category_shop(message)


async def show_category_shop(message: Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, 'Bo`limni tanlang!', reply_markup=buttons_category())


@dp.message_handler(content_types=['text'])
async def get_product_by_category(message: Message):
    chat_id = message.chat.id
    category_text = message.text
    get_product = pars_saber(get_value(category_text))

    for product in get_product:
        images = product.get('images')
        title = product.get('title')
        price = product.get('price')
        link = product.get('link')

        time.sleep(2)

        await message.answer_photo(photo=images, caption=f'''
{title}
{price}''', reply_markup=button_link(link))


executor.start_polling(dp)
