from aiogram import executor
from handler import dp

if __name__ == '__main__':
    executor.start_polling(dp)
