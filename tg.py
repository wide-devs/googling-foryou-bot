from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import keywords, tgtoken

bot = Bot(tgtoken)
dp = Dispatcher(bot)


@dp.message_handler(commands=keywords)
async def google(message=types.Message):
	if message.reply_to_message:
		await message.answer(f"https://google.com/search?q={message.reply_to_message.text}")


if __name__ == "__main__":
	executor.start_polling(dp)
