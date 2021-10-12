from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types,Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from data_base.sqlite_db import sql_add_command
from keyboards import admin_kb
ID = None
class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

#проверка доступа к боту по ID
async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Управляй.', reply_markup = admin_kb.button_case_admin)
    await message.delete()
#Начало диалога загрузки меню
#@dp.message_handler(commands = 'Загрузить',state = None)
async def cm_start(message: types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.photo.set()
        await message.answer('Upload photo')
#режим отмены машины состояний
async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('ok')
#ловим ответ 1 от пользователя и пишем в словарь
#@dp.message_handler(content_types = ['photo'], state = FSMAdmin.photo)
async def load_photo(message: types.Message, state : FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.answer('Enter name position')
    

#ловим ответ 2 от пользователя и пишем в словарь
#@dp.message_handler(state = FSMAdmin.name)
async def load_name(message: types.Message, state : FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdmin.next()
        await message.answer('Enter description')
#ловим ответ 3 от пользователя и пишем в словарь
#@dp.message_handler(state = FSMAdmin.description)
async def load_description(message: types.Message, state : FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
        await FSMAdmin.next()
        await message.answer('Enter price')
#ловим ответ 4 от пользователя и пишем в словарь
#@dp.message_handler(state = FSMAdmin.photo)
async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = float(message.text)
        await message.answer('Done')
        await sqlite_db.sql_add_command(state)
        await state.finish()


#регистрация функций для дальнейшей передачи
def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start,commands = ['Загрузить'],state = None)
    dp.register_message_handler(cancel_handler, Text(equals='отмена',ignore_case=True), state = '*')
    dp.register_message_handler(make_changes_command,commands=['mod'],is_chat_admin=True)
    dp.register_message_handler(load_photo,content_types=['photo'],state = FSMAdmin.photo)
    dp.register_message_handler(load_name,state = FSMAdmin.name)
    dp.register_message_handler(load_description,state = FSMAdmin.description)
    dp.register_message_handler(load_price,state = FSMAdmin.price)
    dp.register_message_handler(cancel_handler, state ="*",commands='отмена')
    