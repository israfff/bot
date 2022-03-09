from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Dispatcher, Bot
import logging

storage = MemoryStorage()

bot = Bot(token='5137555490:AAEZzCm6JSX05Vwp-9WJOK91s53tX_1Asts', parse_mode='HTML')
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)