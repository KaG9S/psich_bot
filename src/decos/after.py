from src.decos.before import *
from src.decos import start

@bot.message_handler(content_types=['text'])
def no_command(message):
    send(message.chat.id, f"Я не можу відповісти на це, може це команда. Якщо я вас раніше попросив написати щось, [звернітся в підтримку](t.me/{consts.admin_u})")

@bot.message_handler()
def no_support(message):
    send(message.chat.id, f"Я не можу відповісти на це повідомлення. Якщо я вас раніше попросив дати мені щось, [звернітся в підтримку](t.me/{consts.admin_u})")
