from flask import Blueprint, request, jsonify

from services.calculos import (
    area_triangulo,
    area_trapezio
)

from utils.validacoes import validar_campos

poligonos_bp = Blueprint(
    "poligonos",
    __name__,
    url_prefix="/poligonos"
)


@poligonos_bp.route("/triangulo", methods=["POST"])
def calcular_triangulo():

    dados = request.get_json(silent=True)

    erro = validar_campos(
        dados,
        ["base", "altura"]
    )

    if erro:
        return jsonify({"erro": erro}), 400

    area = area_triangulo(
        dados["base"],
        dados["altura"]
    )

    return jsonify({
        "figura": "triangulo",
        "base": dados["base"],
        "altura": dados["altura"],
        "area": area
    }), 200


@poligonos_bp.route("/trapezio", methods=["POST"])
def calcular_trapezio():

    dados = request.get_json(silent=True)

    erro = validar_campos(
        dados,
        ["base_maior", "base_menor", "altura"]
    )

    if erro:
        return jsonify({"erro": erro}), 400

    area = area_trapezio(
        dados["base_maior"],
        dados["base_menor"],
        dados["altura"]
    )

    return jsonify({
        "figura": "trapezio",
        "base_maior": dados["base_maior"],
        "base_menor": dados["base_menor"],
        "altura": dados["altura"],
        "area": area
    }), 200