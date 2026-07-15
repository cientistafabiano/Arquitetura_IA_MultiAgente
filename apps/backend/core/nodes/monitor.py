"""Objetivo: Criar o Monitor Node.

Função:
receber a resposta do usuário;
converter para o tipo correto;
atualizar o State."""

from core.catalog import FIELDS


class MonitorNode:

    def update(self, state, field_name, value):

        field = FIELDS[field_name]

        field_type = field["type"]

        if field_type == "float":
            value = float(value)

        elif field_type == "int":
            value = int(value)

        setattr(state, field_name, value)

        return state