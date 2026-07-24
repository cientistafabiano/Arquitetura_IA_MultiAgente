"""DecisionTool será o verdadeiro "cérebro estratégico" do Soberana.

Ela receberá:

preço calculado;  suggested_price
média de mercado;   market_average
margem;
custos;
histórico;
IA preditiva (no futuro).

E responderá algo como:

"Recomenda-se cobrar R$ 182,81. O valor está 3,8% abaixo da média do mercado,
 tornando a clínica mais competitiva sem comprometer a margem."

💡 A partir da DecisionTool, o Soberana deixará de ser uma calculadora e passará
 a ser um verdadeiro Sistema Inteligente de Apoio à Decisão (DSS)

Passo 7a (Sprint 3): valida pré-condições antes de calcular."""

from tools.validation import require


class DecisionTool:

    def execute(self, state):

        require(state, "suggested_price", "market_average")

        difference = state.suggested_price - state.market_average

        if difference < -10:
            decision = (
                "Preço abaixo da média. Boa competitividade."
            )

        elif difference > 10:
            decision = (
                "Preço acima da média. Revisar estratégia."
            )

        else:
            decision = (
                "Preço alinhado ao mercado."
            )

        state.recommendations.append(decision)

        state.decision = decision

        return state