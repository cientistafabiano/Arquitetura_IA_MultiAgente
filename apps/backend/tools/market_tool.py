"""Esta Tool será um diferencial do Soberana.

Ela não calcula preços. Ela fornece contexto para a decisão.

Objetivo: Comparar o preço calculado com o mercado.

Hoje vamos usar um valor fixo. 
Futuramente ela consultará:

Convênios
TUSS
Clínicas da região
Histórico interno
APIs externas"""

class MarketTool:

    def execute(self, state):

        market_average = 190.00

        state.market_average = market_average

        difference = state.suggested_price - market_average

        state.recommendations.append(
            f"Diferença para o mercado: R$ {difference:.2f}"
        )

        return state