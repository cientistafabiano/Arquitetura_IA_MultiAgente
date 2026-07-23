"""graph.py
    │
    ├── cria o StateGraph
    ├── registra os Nodes
    ├── conecta os Nodes
    ├── define START
    ├── define END
    └── compila o grafo
    
Passo 6.1: Criar o StateGraph.

Passo 6.2: Registrar os Nodes.

Passo 6.3: Criar as primeiras arestas (add_edge).

Passo 6.4: Compilar o grafo.

Passo 6.5: Testar.

Só depois seguimos para as conditional_edges."""

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

"""é extremamente importante.
Ela informa ao LangGraph:
"Todo Node deste workflow receberá um objeto do tipo SoberanaState e deverá devolver um SoberanaState."
É isso que permite que o estado seja compartilhado automaticamente entre Planner, Executor e Validator.
Sem essa linha, o LangGraph não sabe qual estrutura de dados está circulando pelo fluxo."""
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