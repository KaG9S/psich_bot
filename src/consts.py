from os import getenv

token = getenv("BOT_TOKEN")
token_u = "your_psich_bot"

admin_u, admin = getenv("ADMIN").split(":")
manag_u, manag = getenv("MANAG").split(":")

sandbox = False
exact_time = False
exact_time_n = 1800
run = True
track_all = False

log_file = "logfile.log"
db_file = "data.db"
