"""
Teste do Passo 6a (Sprint 2 - Consistencia do Contrato).

O que este teste verifica:
Cada etapa do WORKFLOW (core/workflow/workflow.py) tem um campo "tool"
que precisa existir como chave no dicionario ExecutorNode.tools
(core/nodes/executor.py). Antes da correcao do Passo 6a, o WORKFLOW usava
chaves com sufixo "_tool" (ex: "clinical_hour_tool") enquanto o
ExecutorNode usava chaves sem sufixo (ex: "clinical_hour") -- ou seja,
nunca batiam. Isso so nao quebrava porque ainda nao existia nenhuma
ligacao real entre Planner e ExecutorNode usando esse campo.

Como rodar (PowerShell, dentro de apps/backend):
    .venv\\Scripts\\Activate.ps1
    python tests\\test_workflow_consistency.py

Nao usa pytest de proposito -- ainda nao esta no requirements.txt.
E soh um script simples com "assert" e print, prontos para copiar
para pytest mais tarde se o projeto adotar.
"""

import sys
from pathlib import Path

# Garante que "apps/backend" esta no sys.path, nao importa de onde o
# script for chamado (evita depender do diretorio atual do PowerShell).
BACKEND_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND_ROOT))

from core.workflow import WORKFLOW
from core.nodes.executor import ExecutorNode

from core.state import SoberanaState  # adicionar este import no topo do arquivo, junto dos outros
from core.registry import registry  # adicionar junto dos outros imports

# Tools que ainda nao existem de verdade (ex: ReportTool comentado no
# ExecutorNode). Sao esperadas como "ainda nao implementadas", nao como
# falha do teste -- assim o teste nao quebra por causa de um passo futuro
# que ja esta documentado (ver Sprint 3 / ReportTool).
TOOLS_PENDENTES = {"report"}

"""
def test_todo_tool_do_workflow_existe_no_executor():
    executor = ExecutorNode()
    chaves_disponiveis = set(executor.tools.keys())

    erros = []

    for step in WORKFLOW:
        nome_step = step["step"]
        nome_tool = step["tool"]

        if nome_tool in TOOLS_PENDENTES:
            print(f"[PENDENTE] etapa '{nome_step}' -> tool '{nome_tool}' "
                  f"(esperado: ainda nao implementada)")
            continue

        if nome_tool not in chaves_disponiveis:
            erros.append(
                f"etapa '{nome_step}' aponta para tool '{nome_tool}', "
                f"que NAO existe em ExecutorNode.tools "
                f"(chaves disponiveis: {sorted(chaves_disponiveis)})"
            )
        else:
            print(f"[OK] etapa '{nome_step}' -> tool '{nome_tool}'")

    assert not erros, "\n".join(erros)

def test_workflow_output_bate_com_o_que_a_tool_realmente_escreve():
    
    Passo 6b: roda as Tools em sequência sobre um único State (como o
    fluxo real faria) e confere se o campo "output" declarado em cada
    etapa do WORKFLOW é de fato preenchido pela Tool daquela etapa.
    
    state = SoberanaState(
        working_hours=160,
        fixed_costs=12000,
        variable_costs=3500,
        procedure="Limpeza",
        procedure_time=40,
        desired_margin=30,
    )

    executor = ExecutorNode()

    etapas_prontas = [s for s in WORKFLOW if s["tool"] != "report"]  # ReportTool ainda não existe

    for step in etapas_prontas:
        state.next_step = step["tool"]
        state = executor.execute(state)

        valor = getattr(state, step["output"], None)
        assert valor is not None, (
            f"etapa '{step['step']}': campo output '{step['output']}' "
            f"continuou None depois de rodar a tool '{step['tool']}'"
        )
        print(f"[OK] etapa '{step['step']}' -> output '{step['output']}' = {valor}")
"""
def test_todo_tool_do_workflow_existe_no_executor():
    # Passo 6d: as Tools agora vivem no Registry, não mais num dicionário
    # dentro do ExecutorNode. Instanciar ExecutorNode() já garante que
    # register_tools() rodou (ver core/registry/bootstrap.py).
    ExecutorNode()
    chaves_disponiveis = set(registry.tools.keys())

    erros = []

    for step in WORKFLOW:
        nome_step = step["step"]
        nome_tool = step["tool"]

        if nome_tool in TOOLS_PENDENTES:
            print(f"[PENDENTE] etapa '{nome_step}' -> tool '{nome_tool}' "
                  f"(esperado: ainda nao implementada)")
            continue

        if nome_tool not in chaves_disponiveis:
            erros.append(
                f"etapa '{nome_step}' aponta para tool '{nome_tool}', "
                f"que NAO existe no Registry "
                f"(chaves disponiveis: {sorted(chaves_disponiveis)})"
            )
        else:
            print(f"[OK] etapa '{nome_step}' -> tool '{nome_tool}'")

    assert not erros, "\n".join(erros)
def test_workflow_output_bate_com_o_que_a_tool_realmente_escreve():
    
    """Passo 6b: roda as Tools em sequência sobre um único State (como o
    fluxo real faria) e confere se o campo "output" declarado em cada
    etapa do WORKFLOW é de fato preenchido pela Tool daquela etapa."""
    
    state = SoberanaState(
        working_hours=160,
        fixed_costs=12000,
        variable_costs=3500,
        procedure="Limpeza",
        procedure_time=40,
        desired_margin=30,
    )

    executor = ExecutorNode()

    etapas_prontas = [s for s in WORKFLOW if s["tool"] != "report"]  # ReportTool ainda não existe

    for step in etapas_prontas:
        state.next_step = step["tool"]
        state = executor.execute(state)

        valor = getattr(state, step["output"], None)
        assert valor is not None, (
            f"etapa '{step['step']}': campo output '{step['output']}' "
            f"continuou None depois de rodar a tool '{step['tool']}'"
        )
        print(f"[OK] etapa '{step['step']}' -> output '{step['output']}' = {valor}")

if __name__ == "__main__":
    test_todo_tool_do_workflow_existe_no_executor()
    print("\nPasso 6a: todas as etapas do WORKFLOW apontam para uma tool valida no ExecutorNode.")
    test_workflow_output_bate_com_o_que_a_tool_realmente_escreve()
    print("\nPasso 6a e 6b: WORKFLOW consistente com ExecutorNode e com o State.")
    
    

