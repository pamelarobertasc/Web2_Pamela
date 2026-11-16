from flask import Flask
from controllers.evento_controller import evento_bp

from data.banco import iniciar

app = Flask(__name__)
iniciar()
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
