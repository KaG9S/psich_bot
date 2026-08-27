from src.consts import log_file
import inspect
import time

def clear():
    with open(log_file) as f:
        f.write("")

def log(level: int = 1, mes: str = "Something happaned") -> None:
    caller_frame = inspect.currentframe().f_back
    module: str = inspect.currentframe().f_back.f_globals.get('__name__') if caller_frame else "unknown"
    
    level = ["DEBUG", "INFO", "WARNING", "ERROR"][level]
    at_time = time.strftime("%H:%M:%S %m.%d.%Y")
    final_str = f"[{module}] [{level}] [{at_time}] : {mes}"
    with open(log_file, 'a') as f:
        f.write(final_str+'\n')
