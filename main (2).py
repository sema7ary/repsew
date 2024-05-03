import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command


bot = Bot(token='7042594009:AAGgaQtcRvbzVcO7nKlf8-hBNZOA_Li1bGs')
dp = Dispatcher()


@dp.message(Command('start'))
async def cmd_start(message: Message):
	await message.answer('Привет')
	await message.reply('как дела')


@dp.message(Command('help'))
async def cmd_help(message: Message):
	await message.answer('вы нажали на кнопку помощи')


async def main():
	await dp.start_polling(bot)


if __name__ == '__main__':
	try:
		asyncio.run(main())
	except KeyboardInterrupt:
		print('бот выключен')

