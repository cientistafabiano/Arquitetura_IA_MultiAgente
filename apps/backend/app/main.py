from core.state import SoberanaState
from app.graph import graph
from core.nodes import AtendimentoNode, MonitorNode
from core.planner import Planner

def main():
    state = SoberanaState()
    agent = AtendimentoNode()
    monitor = MonitorNode()
    planner = Planner()
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
Pergunta  Tool"""








