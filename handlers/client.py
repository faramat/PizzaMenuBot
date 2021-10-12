from aiogram import types, Dispatcher
from aiogram.types.reply_keyboard import ReplyKeyboardMarkup
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db

#@dp.message_handler(commands=['start','help'])
async def commands_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита', reply_markup=kb_client) #передача клавиатуры при старте
        await message.delete()
    except:
        await message.reply('Напишите боту в личку:\nt.me/aiogramtest12_bot')

#@dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id,'График работы:\nПн-Пт до 23:00. Сб,Вс до 01:00')
    await message.delete()

#@dp.message_handler(commands='Расположение')
async def pizza_place_message(message: types.Message):
    await bot.send_message(message.from_user.id, 'Адрес:\nг. Казань, ул. Школьная, д. 1',reply_markup=ReplyKeyboardRemove()) #delete kb
    await message.delete()

@dp.message_handler(commands=['Меню'])
async def pizza_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)


#регистрация функций для дальнейшей передачи
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start,commands = ['start','help'])
    dp.register_message_handler(pizza_open_command,commands = ['Режим_работы'])
    dp.register_message_handler(pizza_place_message,commands = ['Расположение'])
    dp.register_message_handler(pizza_menu_command,commands=['Меню'])