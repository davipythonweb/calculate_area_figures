# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# -------------------------------------------------------
# Funções de cálculo de área (regra de negócio isolada
# da camada de rotas/API)
# -------------------------------------------------------

def area_triangulo(base, altura):
    """Área do triângulo = (base * altura) / 2"""
    return (base * altura) / 2


def area_trapezio(base_maior, base_menor, altura):
    """Área do trapézio = ((B + b) * h) / 2"""
    return ((base_maior + base_menor) * altura) / 2


def area_retangulo(base, altura):
    """Área do retângulo = base * altura"""
    return base * altura


def area_losango(diagonal_maior, diagonal_menor):
    """Área do losango = (D * d) / 2"""
    return (diagonal_maior * diagonal_menor) / 2


# -------------------------------------------------------
# Função auxiliar para validar campos obrigatórios no JSON
# -------------------------------------------------------

def validar_campos(dados, campos_obrigatorios):
    """
    Verifica se todos os campos obrigatórios estão presentes no JSON
    e se são números válidos. Retorna uma mensagem de erro ou None.
    """
    if dados is None:
        return "Corpo da requisição precisa ser um JSON válido."

    for campo in campos_obrigatorios:
        if campo not in dados:
            return f"Campo obrigatório ausente: '{campo}'"
        if not isinstance(dados[campo], (int, float)):
            return f"Campo '{campo}' deve ser numérico."
        if dados[campo] <= 0:
            return f"Campo '{campo}' deve ser maior que zero."

    return None  # sem erros


# -------------------------------------------------------
# Rotas (endpoints) da API
# -------------------------------------------------------

@app.route('/')
def home():
    """Rota raiz só para confirmar que a API está no ar."""
    return jsonify({
        "mensagem": "API de cálculo de área de polígonos e paralelogramos",
        "endpoints": [
            "/poligonos/triangulo",
            "/poligonos/trapezio",
            "/paralelogramos/retangulo",
            "/paralelogramos/losango"
        ]
    })


@app.route('/poligonos/triangulo', methods=['POST'])
def calcular_triangulo():
    dados = request.get_json(silent=True)  # silent evita erro se não vier JSON
    erro = validar_campos(dados, ['base', 'altura'])

    if erro:
        return jsonify({"erro": erro}), 400  # Bad Request

    area = area_triangulo(dados['base'], dados['altura'])
    return jsonify({
        "figura": "triangulo",
        "base": dados['base'],
        "altura": dados['altura'],
        "area": area
    }), 200


@app.route('/poligonos/trapezio', methods=['POST'])
def calcular_trapezio():
    dados = request.get_json(silent=True)
    erro = validar_campos(dados, ['base_maior', 'base_menor', 'altura'])

    if erro:
        return jsonify({"erro": erro}), 400

    area = area_trapezio(dados['base_maior'], dados['base_menor'], dados['altura'])
    return jsonify({
        "figura": "trapezio",
        "base_maior": dados['base_maior'],
        "base_menor": dados['base_menor'],
        "altura": dados['altura'],
        "area": area
    }), 200


@app.route('/paralelogramos/retangulo', methods=['POST'])
def calcular_retangulo():
    dados = request.get_json(silent=True)
    erro = validar_campos(dados, ['base', 'altura'])

    if erro:
        return jsonify({"erro": erro}), 400

    area = area_retangulo(dados['base'], dados['altura'])
    return jsonify({
        "figura": "retangulo",
        "base": dados['base'],
        "altura": dados['altura'],
        "area": area
    }), 200


@app.route('/paralelogramos/losango', methods=['POST'])
def calcular_losango():
    dados = request.get_json(silent=True)
    erro = validar_campos(dados, ['diagonal_maior', 'diagonal_menor'])

    if erro:
        return jsonify({"erro": erro}), 400

    area = area_losango(dados['diagonal_maior'], dados['diagonal_menor'])
    return jsonify({
        "figura": "losango",
        "diagonal_maior": dados['diagonal_maior'],
        "diagonal_menor": dados['diagonal_menor'],
        "area": area
    }), 200


# -------------------------------------------------------
# Ponto de entrada da aplicação
# -------------------------------------------------------

if __name__ == '__main__':
    # debug=True facilita o desenvolvimento (reload automático e erros detalhados)
    app.run(debug=True, port=5000)