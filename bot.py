from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN
from repo import get_data_from_db, register

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    register(message.from_user.username, message.from_user.id)
    await message.reply("Ты зарегистрировался в системе быстрых оповещений о террористических актах."
                        " Если кто-то укажет тебя в качестве получателя, то в случае террористического "
                        "акта тебе придет сообщение от меня о том кто в опасности и где он находится."
                        "Твоя задача позвонить в полицию в этому случае. Внимание! Бот еще тестируется,"
                        " поэтому просим вас пока не реагировать на его сообщения"
                        "")



@dp.message_handler(commands=['sos'])
async def process_help_command(message: types.Message):
    data = get_data_from_db('@' + message.from_user.username)
    list_of_chat_ids = data[3]
    print(list_of_chat_ids)
    if list_of_chat_ids:
        for user_id in data[3]:
            await bot.send_message(user_id, f'{data[2]} в опастности!')


        await bot.send_message(message.from_user.id, 'Вы отправили сообщение об опастности'
                                                     ' своим контактам')
    else:
        await bot.send_message(message.from_user.id,
                               'Вы не добавили контакты поэтому сообщение SOS никому не отправлено')

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)
