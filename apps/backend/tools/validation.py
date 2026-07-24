"""
Passo 7a (Sprint 3): validação de pré-condição padronizada para as Tools.

Antes desta correção, só a CorrectedCostTool validava os campos que
precisava antes de calcular (com um "if ... raise ValueError" escrito à
mão); as outras deixavam o Python estourar um erro cru (TypeError,
ZeroDivisionError) quando faltava dado. Este módulo centraliza o "como"
validar, pra toda Tool usar do mesmo jeito e levantar o mesmo tipo de
erro, com a mesma mensagem.
"""


class ToolValidationError(ValueError):
    """Erro levantado quando uma Tool não pode calcular por causa de
    dado ausente ou inválido no State."""


def require(state, *field_names):
    """Garante que os campos passados não são None no State.

    Uso: require(state, "fixed_costs", "variable_costs")
    """
    faltando = [
        nome for nome in field_names
        if getattr(state, nome, None) is None
    ]

    if faltando:
        raise ToolValidationError(
            f"Campo(s) obrigatório(s) não informado(s): {', '.join(faltando)}."
        )