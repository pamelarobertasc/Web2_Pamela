from flask import Blueprint, render_template, request, abort, redirect, url_for
from models.evento import Evento
from dao.evento_dao import EventoDAO

evento_bp = Blueprint("evento", __name__)

@evento_bp.route("/eventos", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Model representa um cadastro; a lista guarda o objeto.
        evento = Evento(nome=request.form["nome"], data=request.form["data"],
                        local=request.form["local"])
        EventoDAO.salvar(evento)
        return redirect(url_for("evento.index"))
    return render_template("index.html", eventos=EventoDAO.listar())

@evento_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    evento = EventoDAO.buscar_por_id(id)
    if evento is None:
        abort(404)
    if request.method == "POST":
        EventoDAO.atualizar(evento, request.form["nome"], request.form["data"],
                            request.form["local"])
        return redirect(url_for("evento.index"))
    return render_template("editar.html", evento=evento)

@evento_bp.post("/excluir/<int:id>")
def excluir(id):
    evento = EventoDAO.buscar_por_id(id)
    if evento is None:
        abort(404)
    EventoDAO.excluir(evento)
    return redirect(url_for("evento.index"))
