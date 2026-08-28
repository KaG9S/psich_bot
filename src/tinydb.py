import sqlite3 as sqlite
from src.consts import db_file
from src.loger import log

save_int = 600
conn = sqlite.connect(db_file)
cur = sqlite.Cursor(conn)
changes = 0

def comm():
    global changes
    conn.commit()
    log(0, f"Commited {changes} changes")
    changes = 0

def run(comd, params=None, do_comm=False):
    global changes
    cur.execute(comd, params)
    changes += 1
    log(0, f"Ran command {comd}")
    if do_comm: comm()

def create(tb, data: dict):
    run(f"INSERT INTO {tb} ({str(*data.keys())}) VALUES", tuple(data.values()))

def read(tb, id, coll):
    cur.execute("")

