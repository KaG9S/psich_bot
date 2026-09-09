import src.consts
from src.decos.before import *

def only_admin(**kwargs):
	def real_dec(func):
        @bot.message_handler(**kwargs)
        def wrapper(message):
        	at_time = strftime("%H:%M:%S-%m.%d.%Y")
        	if message.chat.id == consts.admin:
            	log(0, f"Dev command run by admin {consts.admin}")
            	func(message)
            else:
                if consts.track_all:
            	   log(2, f"Someone trying to run dev commands ({consts.admin})")
        return wrapper
    return real_dec
