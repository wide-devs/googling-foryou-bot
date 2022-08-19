from vkbottle.bot import Bot, Message
from vkbottle.dispatch.rules.base import ReplyMessageRule
from config import keywords, vktoken

bot = Bot(vktoken)


@bot.on.message(ReplyMessageRule(), text=keywords)
async def google(message: Message):
	await message.answer(f"https://google.com/search?q={message.reply_to_message.text}")


if __name__ == "__main__":
	bot.run_polling()
