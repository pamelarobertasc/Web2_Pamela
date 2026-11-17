from flask import Flask
from controllers.evento_controller import evento_bp

from extensions import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///eventos.db"
db.init_app(app)
with app.app_context():
    db.create_all()
# Registra as rotas que agora ficam no Controller.
app.register_blueprint(evento_bp)

@app.get("/")
def inicio():
    return "Olá, mundo!"

@app.get("/sobre")
def sobre():
    return "Gestão de Eventos - DW2."

if __name__ == "__main__":
    app.run(debug=True)
