"""Файл для управления запуском ботом."""
import time

from args import namespace
from chests_bot import Bot

bot = Bot(namespace.screen, namespace.chest, namespace.color)

if namespace.debug:
    bot.debug()
else:
    while True:
        time.sleep(60)
        bot.bot_execute()
