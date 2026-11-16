from contextlib import closing
from pathlib import Path
import sqlite3

BANCO = Path(__file__).resolve().parents[1] / "instance" / "eventos.db"

def conectar():
    BANCO.parent.mkdir(exist_ok=True)
    con = sqlite3.connect(BANCO)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA foreign_keys = ON")
    return con

def iniciar():
    esquema = Path(__file__).with_name("schema.sql").read_text(encoding="utf-8")
    with closing(conectar()) as con, con:
        con.executescript(esquema)
