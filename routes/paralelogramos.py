from flask import Blueprint, request, jsonify

# Importação das funções de cálculo de área
from services.calculos import (
    area_retangulo,
    area_losango
)

# Importação da função de validação de campos
from utils.validacoes import validar_campos

# Criação do Blueprint para as rotas de paralelogramos
paralelogramos_bp = Blueprint(
    "paralelogramos",
    __name__,
    url_prefix="/paralelogramos"
)

# Rota para calcular a área do retângulo
@paralelogramos_bp.route("/retangulo", methods=["POST"])
def calcular_retangulo():

    dados = request.get_json(silent=True)

    erro = validar_campos(
        dados,
        ["base", "altura"]
    )

    if erro:
        return jsonify({"erro": erro}), 400

    area = area_retangulo(
        dados["base"],
        dados["altura"]
    )

    return jsonify({
        "figura": "retangulo",
        "base": dados["base"],
        "altura": dados["altura"],
        "area": area
    }), 200

# Rota para calcular a área do losango
@paralelogramos_bp.route("/losango", methods=["POST"])
def calcular_losango():

    dados = request.get_json(silent=True)

    erro = validar_campos(
        dados,
        ["diagonal_maior", "diagonal_menor"]
    )

    if erro:
        return jsonify({"erro": erro}), 400

    area = area_losango(
        dados["diagonal_maior"],
        dados["diagonal_menor"]
    )

    return jsonify({
        "figura": "losango",
        "diagonal_maior": dados["diagonal_maior"],
        "diagonal_menor": dados["diagonal_menor"],
        "area": area
    }), 200

