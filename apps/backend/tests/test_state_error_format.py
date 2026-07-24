"""
Teste do Passo 7b (Sprint 3 - Tratamento de Erro).

Verifica o formato único de erro no SoberanaState: os campos status e
error_message, e o método mark_error() que qualquer Tool/Node vai usar
pra sinalizar falha de forma consistente (a ligação de fato acontece no
Passo 7c).

Como rodar (PowerShell, dentro de apps/backend):
    .venv\\Scripts\\Activate.ps1
    python tests\\test_state_error_format.py
"""
import sys
from pathlib import Path

BACKEND_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND_ROOT))

from core.state import SoberanaState


def test_estado_novo_comeca_sem_erro():
    state = SoberanaState()
    assert state.status == "in_progress"
    assert state.error_message is None
    assert state.has_error is False
    print("[OK] SoberanaState novo começa com status='in_progress' e sem erro.")


def test_mark_error_marca_status_e_mensagem():
    state = SoberanaState()
    state.mark_error("working_hours não pode ser zero.")

    assert state.status == "error"
    assert state.error_message == "working_hours não pode ser zero."
    assert state.has_error is True
    print(f"[OK] mark_error funcionou: status={state.status!r}, error_message={state.error_message!r}")


if __name__ == "__main__":
    test_estado_novo_comeca_sem_erro()
    test_mark_error_marca_status_e_mensagem()
    print("\nPasso 7b: SoberanaState tem um formato único de erro (status + error_message + has_error).")