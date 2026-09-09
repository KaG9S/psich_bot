from src.decos.before import *

@mesh(commands=['start'])
def c_start(message):
    send(message, "Привіт, радий тебе вітати! Що б отримати список дотупних команд введи /help")

@mesh(commands=['help'])
def c_help(message):
    send(message, '''
Список дотупних команд:
/start - Початок роботи / реєстрація
/sess - Записатися на прийом
/mysess - Мої записи
/support - Техничка підтримка
/help - Допомога по командам
''')
