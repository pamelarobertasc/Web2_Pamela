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

    @staticmethod
    def buscar_por_id(id):
        return db.session.get(Evento, id)

    @staticmethod
    def atualizar(evento, nome, data, local):
        evento.nome = nome
        evento.data = data
        evento.local = local
        db.session.commit()

    @staticmethod
    def excluir(evento):
        db.session.delete(evento)
        db.session.commit()
