from contextlib import closing
from data.banco import conectar

class EventoDAO:
    @staticmethod
    def salvar(evento):
        # O bloco com con confirma a escrita se tudo der certo.
        with closing(conectar()) as con, con:
            con.execute("INSERT INTO evento (nome, data, local) VALUES (?, ?, ?)",
                        (evento.nome, evento.data, evento.local))

    @staticmethod
    def listar():
        with closing(conectar()) as con:
            return con.execute("SELECT * FROM evento ORDER BY id").fetchall()
