from aiogram import types, Dispatcher
from create_bot import dp
import json,string

# обработчик мата
#@dp.message_handler()
async def mat_send(message: types.Message):
    if {i.lower().translate(str.maketrans('','', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('mat.json')))) != set():
        await message.bot.send_message(message.from_user.id, 'Не матерись !')
        await message.delete()
#регистрация функций для дальнейшей передачи
def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(mat_send) 