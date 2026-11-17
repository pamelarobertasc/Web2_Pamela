from flask import Blueprint, render_template, request, redirect, url_for
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
