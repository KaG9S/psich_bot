import telebot
from time import sleep, time, strftime
from shutil import move
from src import tinydb
from src.loger import log, clear
from src.decos import before as main_bot
from src.decos import after as loader_bot

timers = []
timers.append( [time() + tinydb.save_int, tinydb.save_int, tinydb.comm] )
timers.append( [time() + 60, 60, (tinydb.comm if tinydb.changes > 20 else ( lambda: log(2, "Not enouth changes to commit automaticaly") ))] )

def tick():
    main_bot.bot.polling()
    for i in range(len(timers)):
        if timers[i][0] > time():
            timers[i][2]()
            timers[i][0] += timers[i][1]
            log(0, f"Timer {i} reset")


if __name__ == "__main__":
    try:
        log(0, "Started succesfully")
        while True:
            tick()
            sleep(0.5)
    except KeyboardInterrupt:
       exit(1) 
    except Exception as e:
        at_time = strftime("%H:%M:%S-%m.%d.%Y")
        log(3, f"{type(e).__name__}: {str(e)}")
        move("logfile.log", f"logs/logfile-{at_time}.log")
