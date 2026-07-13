# deixando Planner inteligente - mostra o estado atual e o q esta faltando para a proxima etapa
from langgraph.graph import StateGraph, END

from core.state import SoberanaState
from core.planner import Planner

planner = Planner()


def planner_node(state: SoberanaState):

    missing = planner.get_missing_fields(state)

    print(f"Etapa: {state.current_step}")
    print(f"Campos faltando: {missing}")

    return state


builder = StateGraph(SoberanaState)

builder.add_node("planner", planner_node)

builder.set_entry_point("planner")

builder.add_edge("planner", END)

graph = builder.compile()

#aqui foi o primeiro comando, mostrando onde esta o atual momento da etapa, e retornando o estado atual
"""from langgraph.graph import StateGraph, END

from core.state import SoberanaState
from core.planner import Planner

planner = Planner()


def planner_node(state: SoberanaState):
    print(f"Etapa atual: {state.current_step}")
    return state


builder = StateGraph(SoberanaState)

builder.add_node("planner", planner_node)

builder.set_entry_point("planner")

builder.add_edge("planner", END)

graph = builder.compile()"""