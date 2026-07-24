"""
Passo 6d (Sprint 2): registra as Tools existentes no Registry central.

Antes desta correção, o ExecutorNode importava e instanciava cada Tool
diretamente, sabendo o nome de cada classe. Isso contrariava o princípio
do projeto: "o LangGraph nunca fala direto com os módulos, só com o
Registry". Esta função concentra o registro num único lugar.
"""

from core.registry import registry
from tools.clinical_hour_tool import ClinicalHourTool
from tools.direct_cost_tool import DirectCostTool
from tools.corrected_cost_tool import CorrectedCostTool
from tools.market_tool import MarketTool
from tools.decision_tool import DecisionTool
#from tools.report_tool import ReportTool


def register_tools():
    registry.register_tool("clinical_hour", ClinicalHourTool())
    registry.register_tool("direct_cost", DirectCostTool())
    registry.register_tool("corrected_cost", CorrectedCostTool())
    registry.register_tool("market", MarketTool())
    registry.register_tool("decision", DecisionTool())
    #registry.register_tool("report", ReportTool())