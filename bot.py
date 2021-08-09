from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Ты зарегистрировался в системе быстрых оповещений о террористических актах."
                        " Если кто-то укажет тебя в качестве получателя, то в случае террористического "
                        "акта тебе придет сообщение от меня о том кто в опасности и где он находится."
                        "Твоя задача позвонить в полицию в этому случае. Внимание! Бот еще тестируется,"
                        " поэтому просим вас пока не реагировать на его сообщения"
                        "")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)
