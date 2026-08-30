import telebot
from time import sleep, time, strftime
from shutil import move
from src import tinydb, timers
from src.loger import log, clear
from src.decos import before as main_bot
from src.decos import after as loader_bot

if __name__ == "__main__":
    try:
        clear()
        timers.timer( tinydb.comm, tinydb.save_int )
        timers.timer( tinydb.comm, 60, (lambda: tinydb.changes > 20) )
        log(1, "Started succesfully")
        while True:
            main_bot.bot.polling()
            timers.tick()
            sleep(0.5)
    except KeyboardInterrupt:
        exit(0) 
    except Exception as e:
        at_time = strftime("%H:%M:%S-%m.%d.%Y")
        log(3, f"{type(e).__name__}: {str(e)}")
        move("logfile.log", f"logs/logfile-{at_time}.log")
