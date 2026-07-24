"""
Teste do Passo 7c (Sprint 3 - Tratamento de Erro).

Verifica que o ExecutorNode captura ToolValidationError e traduz pro
formato padronizado do State (status="error" + error_message), em vez de
deixar a exceção propagar crua — e que o caminho feliz continua igual.

Como rodar (PowerShell, dentro de apps/backend):
    .venv\\Scripts\\Activate.ps1
    python tests\\test_executor_error_handling.py
"""
import sys
from pathlib import Path

BACKEND_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND_ROOT))

from core.state import SoberanaState
from core.nodes.executor import ExecutorNode


def test_executor_traduz_erro_de_tool_para_o_state():
    state = SoberanaState()  # nenhum dado preenchido
    state.next_step = "clinical_hour"

    executor = ExecutorNode()
    state = executor.execute(state)  # antes desta correção, isso quebrava aqui

    assert state.has_error is True
    assert state.status == "error"
    assert state.error_message is not None
    print(f"[OK] ExecutorNode traduziu o erro: status={state.status!r}, error_message={state.error_message!r}")


def test_executor_ainda_funciona_no_caminho_feliz():
    state = SoberanaState(
        working_hours=160,
        fixed_costs=12000,
        variable_costs=3500,
    )
    state.next_step = "clinical_hour"

    executor = ExecutorNode()
    state = executor.execute(state)

    assert state.has_error is False
    assert state.clinical_hour is not None
    print(f"[OK] caminho feliz continua funcionando: clinical_hour={state.clinical_hour}")


if __name__ == "__main__":
    test_executor_traduz_erro_de_tool_para_o_state()
    test_executor_ainda_funciona_no_caminho_feliz()
    print("\nPasso 7c: ExecutorNode captura erro de Tool e traduz pro formato padronizado do State.")