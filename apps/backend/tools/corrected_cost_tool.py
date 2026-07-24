"""calcula o preço mínimo sustentável.

Inicialmente vamos usar: Preço Corrigido = Custo Direto x (1 + Margem)

Mais tarde adicionaremos:
impostos
inadimplência
risco
ocupação
inflação
custos financeiros

Passo 7a (Sprint 3): a validação manual daqui virou o modelo pro helper
compartilhado tools/validation.py — agora usa o mesmo helper das outras
Tools, em vez de checks feitos à mão."""

from tools.validation import require


class CorrectedCostTool:

    def execute(self, state):

        require(state, "direct_cost", "desired_margin")

        corrected_cost = (
            state.direct_cost
            * (1 + state.desired_margin / 100)
        )

        state.suggested_price = corrected_cost

        state.recommendations.append(
            f"Preço sugerido: R$ {corrected_cost:.2f}"
        )

        return state