"""Objetivo: Calcular o custo direto do procedimento.

Fórmula inicial: Custo Direto = Hora Clínica x Tempo do Procedimento

Passo 7a (Sprint 3): valida pré-condições antes de calcular."""

from tools.validation import require


class DirectCostTool:

    def execute(self, state):

        require(state, "clinical_hour", "procedure_time")

        direct_cost = (
            state.clinical_hour * state.procedure_time
        ) / 60

        state.direct_cost = direct_cost

        state.recommendations.append(
            f"Custo direto: R$ {direct_cost:.2f}"
        )

        return state