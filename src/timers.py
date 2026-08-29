import time
from src.loger import log

timers = []

def timer(func, cool: float | int = 60, cond = (lambda: True)):
    global timers
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    timers.append( [time.time() + cool, cool, wrapper] )
    log(0, f"New timer {len(timers)}: cooldown={cool}s, function={func.__name__}, condition={"true" if cond == (lambda: True) else "not true"}")
    return wrapper

def tick(which = range(len(timers))):
    global timers
    for i in which:
        if timers[i][0] > time.time():
            timers[i][2]()
            timers[i][0] += timers[i][1]
            log(0, f"Timer {i} reset")
