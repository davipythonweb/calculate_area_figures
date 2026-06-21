"""
Funções auxiliares de validação.
"""


def validar_campos(dados, campos_obrigatorios):
    """
    Verifica se todos os campos obrigatórios estão presentes
    e se possuem valores numéricos maiores que zero.

    Retorna:
        None -> se não houver erros
        str  -> mensagem de erro
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

    return None