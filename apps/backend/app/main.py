from core.state import SoberanaState
from app.graph import graph
from core.nodes import AtendimentoNode, MonitorNode
from core.planner import Planner
from tools.clinical_hour_tool import ClinicalHourTool
from tools.direct_cost_tool import DirectCostTool
from tools.corrected_cost_tool import CorrectedCostTool
from tools.market_tool import MarketTool
from tools.decision_tool import DecisionTool



def main():
    state = SoberanaState()
    agent = AtendimentoNode()
    monitor = MonitorNode()
    planner = Planner()
    tool = ClinicalHourTool()
    tol = DirectCostTool()
    corrected = CorrectedCostTool()
    market = MarketTool()
    decision = DecisionTool()
    result = graph.invoke(state)
    print(result)
    print("-------------------------")
    print(agent.ask("working_hours"))
    print("-------------------------")
    state = monitor.update(state, "working_hours", "160")
    print(state.working_hours)
    print("-------------------------")
    print(planner.get_missing_fields(state))
    state = monitor.update(state, "fixed_costs", "12000")
    state = monitor.update(state, "variable_costs", "3000")
    print("-------------------------")
    print(planner.get_missing_fields(state))
    print("-------------------------")
    print(planner.should_execute_tool(state))
    print("-------------------------")
    state.fixed_costs = 12000
    state.variable_costs = 3000
    state.working_hours = 160
    state.procedure_time = 90
    tool.execute(state)
    print(state.clinical_hour)
    print("-------------------------")
    tol.execute(state)
    print(state.direct_cost)
    print("-------------------------")
    state.desired_margin = 30
    corrected.execute(state)
    print(state.suggested_price)
    print("-------------------------")
    market.execute(state)
    print(state.market_average)
    print("-------------------------")
    decision.execute(state)
    print(state.decision)

"""O que aconteceu?

Antes:

Planner
    ↓
Campos faltando

Agora:

Planner
    ↓
Campos completos?
    │
 ┌──┴──┐
 │     │
Não   Sim
 │     │
 ▼     ▼
Pergunta  Tool

com clical_hour:
Planner
     │
     ▼
Todos os campos preenchidos?
     │
    Sim
     │
     ▼
ClinicalHourTool
     │
Calcula Hora Clínica
     │
Atualiza State
     │
     ▼
Planner

Observação de arquitetura

A partir de agora, toda regra de negócio será implementada em uma Tool.

Assim:

Nodes → tomam decisões e conversam.
Tools → executam cálculos, integrações e regras de negócio.
State → guarda os resultados.
Planner → decide o próximo passo.

Esse é exatamente o padrão recomendado para projetos com LangGraph e deixará a 
arquitetura da Soberana organizada e fácil de evoluir.

Arquitetura - criando uma separação

ClinicalHourTool
        │
        ▼
DirectCostTool
        │
        ▼
CorrectedCostTool
        │
        ▼
MarketTool
        │
        ▼
DecisionTool

Isso é exatamente o que queríamos desde o início: cada Tool resolve um único problema, 
enquanto o LangGraph apenas orquestra o fluxo.

📌 Observação importante

Estamos chegando ao ponto em que o projeto deixará de ser um conjunto de componentes e
passará a funcionar como um pipeline completo dentro do LangGraph.

Depois da ReportTool, faremos uma pequena refatoração para que o Planner execute
automaticamente cada Tool, sem precisarmos chamá-las manualmente no main.py. 
A partir daí, o LangGraph assumirá de fato a orquestração do fluxo, que sempre foi o objetivo da arquitetura."""








