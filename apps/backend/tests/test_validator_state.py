"""
Teste do Passo 6c (Sprint 2 - Consistência do Contrato).

Verifica que:
1. SoberanaState aceita o campo validation_errors sem erro do Pydantic
   (antes desta correção, ValidatorNode.execute() quebrava ao tentar
   atribuir um campo que o modelo não conhecia).
2. ValidatorNode reporta erro quando a etapa não produziu o output
   esperado, e não reporta nada quando produziu.

Como rodar (PowerShell, dentro de apps/backend):
    .venv\\Scripts\\Activate.ps1
    python tests\\test_validator_state.py
"""
import sys
from pathlib import Path

BACKEND_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND_ROOT))

from core.state import SoberanaState
from core.nodes.validator import ValidatorNode


def test_validator_nao_quebra_e_nao_acusa_erro_quando_output_existe():
    state = SoberanaState(current_step="clinical_hour", clinical_hour=42.0)
    validator = ValidatorNode()

    state = validator.execute(state)  # antes desta correção, quebrava aqui

    assert state.validation_errors == [], (
        f"esperava lista vazia, veio: {state.validation_errors}"
    )
    print("[OK] ValidatorNode não quebra e não acusa erro quando o output existe.")


def test_validator_acusa_erro_quando_output_falta():
    state = SoberanaState(current_step="clinical_hour")  # clinical_hour continua None

    validator = ValidatorNode()
    state = validator.execute(state)

    assert state.validation_errors, "esperava pelo menos 1 erro, veio lista vazia"
    print(f"[OK] ValidatorNode acusou corretamente: {state.validation_errors}")


if __name__ == "__main__":
    test_validator_nao_quebra_e_nao_acusa_erro_quando_output_existe()
    test_validator_acusa_erro_quando_output_falta()
    print("\nPasso 6c: SoberanaState aceita validation_errors e ValidatorNode funciona sem quebrar.")