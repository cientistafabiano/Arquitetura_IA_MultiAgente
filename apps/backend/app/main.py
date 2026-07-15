from core.state import SoberanaState
from app.graph import graph
from core.nodes import AtendimentoNode, MonitorNode

def main():
    state = SoberanaState()
    agent = AtendimentoNode()
    monitor = MonitorNode()
    result = graph.invoke(state)
    print(result)
    print("-------------------------")
    print(agent.ask("working_hours"))
    print("-------------------------")
    state = monitor.update(state, "working_hours", "160")
    print(state.working_hours)




