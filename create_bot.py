#импорт токена
from aiogram import Bot
from aiogram.dispatcher import Dispatcher, storage
from tg_token import API_TOKEN
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage #хранение в оперативке

storage=MemoryStorage()
#инициализация бота
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot,storage=storage) 
 