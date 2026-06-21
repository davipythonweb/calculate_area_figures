from flask import Blueprint, jsonify

home_bp = Blueprint("home", __name__)


@home_bp.route("/", methods=["GET"])
def home():
    return jsonify({
        "mensagem": "API de cálculo de área de polígonos e paralelogramos",
        "endpoints": [
            "/poligonos/triangulo",
            "/poligonos/trapezio",
            "/paralelogramos/retangulo",
            "/paralelogramos/losango"
        ]
    }), 200