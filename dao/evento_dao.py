from extensions import db
from models.evento import Evento

class EventoDAO:
    @staticmethod
    def salvar(evento):
        db.session.add(evento)
        db.session.commit()

    @staticmethod
    def listar():
        return db.session.scalars(db.select(Evento).order_by(Evento.id)).all()
