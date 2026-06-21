from flask import Blueprint, request, jsonify

# Importação das funções de cálculo de área
from services.calculos import (
    area_triangulo,
    area_trapezio
)

# Importação da função de validação de campos
from utils.validacoes import validar_campos

# Criação do Blueprint para as rotas de polígonos
poligonos_bp = Blueprint(
    "poligonos",
    __name__,
    url_prefix="/poligonos"
)


# Rota para calcular a área do triângulo
@poligonos_bp.route("/triangulo", methods=["POST"])
def calcular_triangulo():

    # Obtém os dados enviados no corpo da requisição
    dados = request.get_json(silent=True)

    # Valida os campos necessários para o cálculo da área do triângulo
    erro = validar_campos(
        dados,
        ["base", "altura"]
    )

    # Se houver algum erro na validação, retorna uma resposta de erro com status 400
    if erro:
        return jsonify({"erro": erro}), 400

    # Calcula a área do triângulo utilizando a função importada
    area = area_triangulo(
        dados["base"],
        dados["altura"]
    )

    # Retorna a resposta com os dados da figura e a área calculada
    return jsonify({
        "figura": "triangulo",
        "base": dados["base"],
        "altura": dados["altura"],
        "area": area
    }), 200


# Rota para calcular a área do trapézio
@poligonos_bp.route("/trapezio", methods=["POST"])
def calcular_trapezio():

    # Obtém os dados enviados no corpo da requisição
    dados = request.get_json(silent=True)

    # 
    erro = validar_campos(
        dados,
        ["base_maior", "base_menor", "altura"]
    )

    # Se houver algum erro na validação, retorna uma resposta de erro com status 400
    if erro:
        return jsonify({"erro": erro}), 400

    # Calcula a área do trapézio utilizando a função importada
    area = area_trapezio(
        dados["base_maior"],
        dados["base_menor"],
        dados["altura"]
    )

    # Retorna a resposta com os dados da figura e a área calculada
    return jsonify({
        "figura": "trapezio",
        "base_maior": dados["base_maior"],
        "base_menor": dados["base_menor"],
        "altura": dados["altura"],
        "area": area
    }), 200