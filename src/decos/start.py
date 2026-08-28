from src.decos.before import *

@bot.message_handler(commands=['start'])
def c_start(message):
    send(message, "Привіт, радий тебе вітати! Що б отримати список дотупних команд введи /help")
