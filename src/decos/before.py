import telebot
from telebot import types
from src import consts
from src.loger import log
import random
from time import strftime
import json

bot = telebot.TeleBot(consts.token)

def send(to: int, message: str, reply_kb=None, reply_to=None):
    if type(to) == types.Message:
        to: int = to.chat.id
    else:
        to: int = to
    log(1, f"Send message to {to}")
    bot.send_message(to, message, parse_mode="markdown", reply_markup=reply_kb, reply_to_message_id=reply_to, disable_web_page_preview=True)

def are_you_sure(
    callback_yes: str, callback_no: str,
    texts_yes: list[str] = ["Так, я впевнений/-на", "Так, я точно впевнений/-на"], texts_no: list[str] = ["Ні, я не до кінця впевнений/-на", "Звісно ні!!!", "Не впевнений"]
    ):
    kb = types.InlineKeyboardMarkup()
    but_text = texts_yes+texts_no
    random.shuffle(but_text)
    for i in but_text:
        kb.add(
            types.InlineKeyboardButton(i,
            callback_data=callback_yes if (i in texts_yes) else callback_no)
        )
    return kb

mesh = bot.message_handler
if consts.track_all:
    def mesh(**kwargs):
        def real_dec(func):
            @bot.message_handler(**kwargs)
            def wrapper(message):
                at_time = strftime("%H:%M:%S-%m.%d.%Y")
                log(1, f"Reciived message from {message.chat.id}{' @'+message.chat.username if message.chat.username else ''} type={message.content_type}{'' if message.content_type!="text" else ', '+message.text}")
                if message.content_type != "text":
                    with open(f"logs/message-{message.chat.id}-{at_time}.json", 'w') as f:
                        f.write(json.dumps(message.json, indent=4, sort_keys=True, ensure_ascii=False))
                func(message)
            return wrapper
        return real_dec
