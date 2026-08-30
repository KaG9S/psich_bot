from os import getenv

token = getenv("BOT_TOKEN")
token_u = "your_psich_bot"

admin_u, admin = getenv("ADMIN").split(":")
psich_u, psich = getenv("PSICH").split(":")

sandbox = False
exact_time = False
exact_time_n = 1800

log_file = "logfile.log"
db_file = "data.db"
