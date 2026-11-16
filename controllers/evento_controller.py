from flask import Blueprint, render_template, request, redirect, url_for
from models.evento import Evento
from data.memoria import eventos

evento_bp = Blueprint("evento", __name__)

@evento_bp.route("/eventos", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Model representa um cadastro; a lista guarda o objeto.
        evento = Evento(request.form["nome"], request.form["data"],
                        request.form["local"])
        eventos.append(evento)
        return redirect(url_for("evento.index"))
    return render_template("index.html", eventos=eventos)
