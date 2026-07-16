from core.state import SoberanaState
from app.graph import graph
from core.nodes import AtendimentoNode, MonitorNode
from core.planner import Planner
from tools.clinical_hour_tool import ClinicalHourTool




def main():
    state = SoberanaState()
    agent = AtendimentoNode()
    monitor = MonitorNode()
    planner = Planner()
    tool = ClinicalHourTool()
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
    tool.execute(state)
    print(state.clinical_hour)


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

Esse é exatamente o padrão recomendado para projetos com LangGraph e deixará a arquitetura da Soberana organizada e fácil de evoluir."""








