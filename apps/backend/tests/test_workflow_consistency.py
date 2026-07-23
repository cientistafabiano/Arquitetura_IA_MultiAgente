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


# Tools que ainda nao existem de verdade (ex: ReportTool comentado no
# ExecutorNode). Sao esperadas como "ainda nao implementadas", nao como
# falha do teste -- assim o teste nao quebra por causa de um passo futuro
# que ja esta documentado (ver Sprint 3 / ReportTool).
TOOLS_PENDENTES = {"report"}


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


if __name__ == "__main__":
    test_todo_tool_do_workflow_existe_no_executor()
    print("\nPasso 6a: todas as etapas do WORKFLOW apontam para uma tool valida no ExecutorNode.")
