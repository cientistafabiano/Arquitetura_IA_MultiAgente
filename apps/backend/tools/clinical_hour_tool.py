"""Objetivo: Calcular a Hora Clínica.

Fórmula inicial: Hora Clínica = (Custos Fixos + Custos Variáveis) / Horas Produtivas"""

class ClinicalHourTool:

    def execute(self, state):

        clinical_hour = (
            state.fixed_costs + state.variable_costs
        ) / state.working_hours

        state.recommendations.append(
            f"Hora clínica calculada: R$ {clinical_hour:.2f}"
        )

        state.clinical_hour = clinical_hour

        return state