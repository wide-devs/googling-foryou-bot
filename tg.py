from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import *

bot = Bot(tgtoken)
dp = Dispatcher(bot)


@dp.message_handler(commands=google)
async def google(message=types.Message):
	link = "https://google.com/search?q="
	args = message.get_args()
	if message.reply_to_message:
		await message.answer(f"{link}{message.reply_to_message.text}")
	elif args:
		await message.answer(f"{link}{args}")


@dp.message_handler(commands=yandex)
async def yandex(message=types.Message):
	link = "https://yandex.ru/search/?text="
	args = message.get_args()
	if message.reply_to_message:
		await message.answer(f"{link}{message.reply_to_message.text}")
	elif args:
		await message.answer(f"{link}{args}")


@dp.message_handler(commands=duckduckgo)
async def yandex(message=types.Message):
	link = "https://duckduckgo.com/?q="
	args = message.get_args()
	if message.reply_to_message:
		await message.answer(f"{link}{message.reply_to_message.text}")
	elif args:
		await message.answer(f"{link}{args}")


@dp.message_handler(commands=bing)
async def yandex(message=types.Message):
	link = "https://www.bing.com/search?q="
	args = message.get_args()
	if message.reply_to_message:
		await message.answer(f"{link}{message.reply_to_message.text}")
	elif args:
		await message.answer(f"{link}{args}")



if __name__ == "__main__":
	executor.start_polling(dp)
