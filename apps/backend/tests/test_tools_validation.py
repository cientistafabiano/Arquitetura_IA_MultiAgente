"""
Teste do Passo 7a (Sprint 3 - Tratamento de Erro).

Verifica que toda Tool valida suas pré-condições antes de calcular, e
levanta ToolValidationError (não um erro cru do Python) quando falta
dado — e que o caminho feliz (todos os dados presentes) continua
funcionando normalmente.

Como rodar (PowerShell, dentro de apps/backend):
    .venv\\Scripts\\Activate.ps1
    python tests\\test_tools_validation.py
"""
import sys
from pathlib import Path

BACKEND_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BACKEND_ROOT))

from core.state import SoberanaState
from tools.validation import ToolValidationError
from tools.clinical_hour_tool import ClinicalHourTool
from tools.direct_cost_tool import DirectCostTool
from tools.corrected_cost_tool import CorrectedCostTool
from tools.market_tool import MarketTool
from tools.decision_tool import DecisionTool


def test_clinical_hour_tool_acusa_campo_faltando():
    state = SoberanaState()
    try:
        ClinicalHourTool().execute(state)
        assert False, "esperava ToolValidationError, tool executou sem erro"
    except ToolValidationError as erro:
        print(f"[OK] ClinicalHourTool acusou: {erro}")


def test_clinical_hour_tool_acusa_working_hours_zero():
    state = SoberanaState(fixed_costs=1000, variable_costs=500, working_hours=0)
    try:
        ClinicalHourTool().execute(state)
        assert False, "esperava ToolValidationError, tool executou sem erro"
    except ToolValidationError as erro:
        print(f"[OK] ClinicalHourTool acusou working_hours=0: {erro}")


def test_direct_cost_tool_acusa_campo_faltando():
    state = SoberanaState()
    try:
        DirectCostTool().execute(state)
        assert False, "esperava ToolValidationError, tool executou sem erro"
    except ToolValidationError as erro:
        print(f"[OK] DirectCostTool acusou: {erro}")


def test_corrected_cost_tool_acusa_campo_faltando():
    state = SoberanaState()
    try:
        CorrectedCostTool().execute(state)
        assert False, "esperava ToolValidationError, tool executou sem erro"
    except ToolValidationError as erro:
        print(f"[OK] CorrectedCostTool acusou: {erro}")


def test_market_tool_acusa_campo_faltando():
    state = SoberanaState()
    try:
        MarketTool().execute(state)
        assert False, "esperava ToolValidationError, tool executou sem erro"
    except ToolValidationError as erro:
        print(f"[OK] MarketTool acusou: {erro}")


def test_decision_tool_acusa_campo_faltando():
    state = SoberanaState()
    try:
        DecisionTool().execute(state)
        assert False, "esperava ToolValidationError, tool executou sem erro"
    except ToolValidationError as erro:
        print(f"[OK] DecisionTool acusou: {erro}")


def test_fluxo_completo_ainda_funciona_com_dados_validos():
    """Garante que a validação não quebrou o caminho feliz (mesmo cenário do Passo 6b)."""
    state = SoberanaState(
        working_hours=160,
        fixed_costs=12000,
        variable_costs=3500,
        procedure="Limpeza",
        procedure_time=40,
        desired_margin=30,
    )

    state = ClinicalHourTool().execute(state)
    state = DirectCostTool().execute(state)
    state = CorrectedCostTool().execute(state)
    state = MarketTool().execute(state)
    state = DecisionTool().execute(state)

    assert state.decision is not None
    print(f"[OK] fluxo completo com dados válidos ainda funciona: {state.decision}")


if __name__ == "__main__":
    test_clinical_hour_tool_acusa_campo_faltando()
    test_clinical_hour_tool_acusa_working_hours_zero()
    test_direct_cost_tool_acusa_campo_faltando()
    test_corrected_cost_tool_acusa_campo_faltando()
    test_market_tool_acusa_campo_faltando()
    test_decision_tool_acusa_campo_faltando()
    test_fluxo_completo_ainda_funciona_com_dados_validos()
    print("\nPasso 7a: todas as Tools validam suas pré-condições de forma consistente.")