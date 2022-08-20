from vkbottle.bot import Bot, Message
from vkbottle.dispatch.rules.base import ReplyMessageRule
from config import *

bot = Bot(vktoken)


@bot.on.message(ReplyMessageRule(), text=google)
async def google(message: Message):
	if ggl:
		link = "https://google.com/search?q="
		await message.answer(f"{link}{message.reply_to_message.text}")


@bot.on.message(ReplyMessageRule(), text=yandex)
async def google(message: Message):
	if ydx:
		link = "https://yandex.ru/search/?text="
		await message.answer(f"{link}{message.reply_to_message.text}")


@bot.on.message(ReplyMessageRule(), text=duckduckgo)
async def google(message: Message):
	if ddg:
		link = "https://duckduckgo.com/?q="
		await message.answer(f"{link}{message.reply_to_message.text}")


@bot.on.message(ReplyMessageRule(), text=bing)
async def google(message: Message):
	if bing:
		link = "https://www.bing.com/search?q="
		await message.answer(f"{link}{message.reply_to_message.text}")


if __name__ == "__main__":
	bot.run_polling()
