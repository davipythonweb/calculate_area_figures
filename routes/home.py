from flask import Blueprint, jsonify

# Criação do Blueprint para a rota home
home_bp = Blueprint("home", __name__)


# Rota para a página inicial da API
@home_bp.route("/", methods=["GET"])
def home():
    return jsonify({
        "mensagem": "API de calculo de area de polagonos e paralelogramos",
        "endpoints": [
            "/poligonos/triangulo",
            "/poligonos/trapezio",
            "/paralelogramos/retangulo",
            "/paralelogramos/losango"
        ]
    }), 200