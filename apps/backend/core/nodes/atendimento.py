"""
Objetivo: O Atendimento não toma decisões.

Ele apenas:
recebe do Planner qual campo falta;
consulta o Field Catalog;
monta a pergunta para o usuário.
"""
from core.catalog import FIELDS


class AtendimentoNode:

    def ask(self, field_name: str):

        field = FIELDS[field_name]

        return {
            "field": field_name,
            "question": field["question"],
            "unit": field["unit"],
            "example": field["example"],
        }
    

"""Neste momento, o Atendimento ainda não usa IA.

Isso foi intencional.

Assim economizamos chamadas ao modelo. Quando integrarmos a OpenAI, o Atendimento poderá transformar essa pergunta em algo mais natural, por exemplo:

"Para calcular corretamente sua hora clínica, preciso saber quantas horas produtivas sua clínica possui por mês. Informe apenas o número de horas. Exemplo: 160."

Mas a lógica continuará sendo a mesma: o Planner decide, o Atendimento comunica."""