import telebot
from time import sleep, time
from src import *
from src.loger import log
from src.decos import main

if __name__ == "__main__":
    try:
        while True:
            main.bot.polling()
            sleep(0.5)
    except Exception as e:
        log(3, f"{type(e).__name__}: {str(e)}")
