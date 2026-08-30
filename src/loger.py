from src.consts import log_file
import inspect
import time

def clear():
    at_time = time.strftime("%H:%M:%S %m.%d.%Y")
    caller_frame = inspect.currentframe().f_back
    module: str = inspect.currentframe().f_back.f_globals.get('__name__') if caller_frame else "unknown"
    with open(log_file, 'w') as f:
        f.write("")
        log(2, "Logs cleared, this is new log")

def log(level: int = 1, mes: str = "Something happaned") -> None:
    at_time = time.strftime(f"%H:%M:{time.time() % 60} %m.%d.%Y")
    caller_frame = inspect.currentframe().f_back
    module: str = inspect.currentframe().f_back.f_globals.get('__name__') if caller_frame else "unknown"
    level = ["DEBUG", "INFO", "WARN", "ERROR"][level]
    final_str = f"[{level}] [{at_time}] [{module}] : {mes}"
    with open(log_file, 'a') as f:
        f.write(final_str+'\n')
    print(final_str)
