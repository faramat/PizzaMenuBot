from aiogram.types import ReplyKeyboardMarkup, KeyboardButton#, ReplyKeyboardRemove

b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Расположение')
b3 = KeyboardButton('/Меню')
#b4 = KeyboardButton('Поделиться номером', request_contact=True)
#b5 = KeyboardButton('Отправить местоположение', request_location=True)

#замена обычной клавиатуры
kb_client = ReplyKeyboardMarkup(resize_keyboard=True) #one_time_keyboard=True - cпрятать кб после 1 нажатия
#add добавление кнопки с новой строки, insert - сосед, row - строка
#kb_client.add(b1).add(b2).insert(b3)
kb_client.add(b1).add(b2).add(b3)#.row(b4,b5)
