"""
Teste do Passo 7d (Sprint 3 - Tratamento de Erro).

Verifica a regra definida: quando o Validator encontra um problema, ele
marca o State como erro (mesmo formato do Passo 7b/7c) e current_step não
avança. Quando está tudo certo, não marca erro.

Como rodar (PowerShell, dentro de apps/backend):
    .venv\\Scripts\\Activate.ps1
    python tests\\test_validator_error_rule.py
"""
import sys
from pathlib import Path

BACKEND_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND_ROOT))

from core.state import SoberanaState
from core.nodes.validator import ValidatorNode


def test_validator_marca_erro_quando_output_falta():
    state = SoberanaState(current_step="clinical_hour")  # clinical_hour continua None
    etapa_antes = state.current_step

    validator = ValidatorNode()
    state = validator.execute(state)

    assert state.has_error is True
    assert state.current_step == etapa_antes, "current_step não deveria avançar quando há erro"
    print(f"[OK] Validator marcou erro e não avançou a etapa: {state.error_message!r}")


def test_validator_nao_marca_erro_quando_output_existe():
    state = SoberanaState(current_step="clinical_hour", clinical_hour=42.0)

    validator = ValidatorNode()
    state = validator.execute(state)

    assert state.has_error is False
    print("[OK] Validator não marcou erro quando o output existe.")


if __name__ == "__main__":
    test_validator_marca_erro_quando_output_falta()
    test_validator_nao_marca_erro_quando_output_existe()
    print("\nPasso 7d: Validator segue a regra definida — marca erro e não avança etapa.")