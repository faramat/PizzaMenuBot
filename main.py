#импорт необходимых модулей для работы
from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db
# Служебная информация
async def on_startup(_):
    print('Bot online. OK!')
    sqlite_db.sql_start()
#импорт хендлеров
from handlers import client, admin, other

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)


# start polling
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True,on_startup=on_startup)