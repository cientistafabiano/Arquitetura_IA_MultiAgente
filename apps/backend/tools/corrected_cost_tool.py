"""calcula o preço mínimo sustentável.

Inicialmente vamos usar: Preço Corrigido = Custo Direto x (1 + Margem)

Mais tarde adicionaremos:
impostos
inadimplência
risco
ocupação
inflação
custos financeiros"""
class CorrectedCostTool:

    def execute(self, state):

        if state.direct_cost is None:
            raise ValueError("Custo direto não calculado.")

        if state.desired_margin is None:
            raise ValueError("Margem não informada.")

        corrected_cost = (
            state.direct_cost
            * (1 + state.desired_margin / 100)
        )

        state.suggested_price = corrected_cost

        state.recommendations.append(
            f"Preço sugerido: R$ {corrected_cost:.2f}"
        )

        return state