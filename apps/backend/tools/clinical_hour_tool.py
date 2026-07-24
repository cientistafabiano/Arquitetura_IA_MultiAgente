"""Objetivo: Calcular a Hora Clínica.

Fórmula inicial: Hora Clínica = 
(Custos Fixos + Custos Variáveis) /
 Horas Produtivas
 
 recebe o state;
✅ lê informações do state;
✅ realiza o cálculo;
✅ atualiza o state;
✅ retorna o state.

Passo 7a (Sprint 3): valida pré-condições antes de calcular, usando o
helper compartilhado tools/validation.py — mesmo padrão de todas as
outras Tools."""
from tools.validation import require, ToolValidationError

class ClinicalHourTool:

    def execute(self, state):

        require(state, "fixed_costs", "variable_costs", "working_hours")

        if state.working_hours == 0:
            raise ToolValidationError("working_hours não pode ser zero.")

        clinical_hour = (
            state.fixed_costs + state.variable_costs
        ) / state.working_hours

        state.recommendations.append(
            f"Hora clínica calculada: R$ {clinical_hour:.2f}"
        )

        state.clinical_hour = clinical_hour

        return state








