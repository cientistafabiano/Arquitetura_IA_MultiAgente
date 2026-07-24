"""Objetivo: Criar o primeiro nó inteligente do workflow: ExecutorNode.

A responsabilidade dele será:

receber o nome da ferramenta que deve ser executada;
localizar a classe correspondente;
executar a ferramenta;
devolver o resultado para o estado do LangGraph.

Assim, nenhum outro componente precisará conhecer as ferramentas diretamente."""
from tools.clinical_hour_tool import ClinicalHourTool
from tools.direct_cost_tool import DirectCostTool
from tools.corrected_cost_tool import CorrectedCostTool
from tools.market_tool import MarketTool
from tools.decision_tool import DecisionTool
#from tools.report_tool import ReportTool

class ExecutorNode:

    def __init__(self):

        # As chaves abaixo precisam bater exatamente com o campo "tool"
        # de cada etapa em core/workflow/workflow.py (WORKFLOW).
        # Convenção (Passo 6a, Sprint 2): sem sufixo "_tool" na chave —
        # a classe já deixa claro que é uma Tool (ex: ClinicalHourTool).
        self.tools = {
            "clinical_hour": ClinicalHourTool(),
            "direct_cost": DirectCostTool(),
            "corrected_cost": CorrectedCostTool(),
            "market": MarketTool(),
            "decision": DecisionTool(),
            #"report": ReportTool(),
        }

    def execute(self, state):

        #Ler o próximo passo
        #next_step = state["next_step"]
        #Procurar a ferramenta
        tool = self.tools[state.next_step]
        #Executar a ferramenta
        #result = tool.run(state)
        #Atualizar o estado
        #state["last_result"] = result
        #retornar o estado atualizado
        return tool.execute(state)

"""
Essa implementação deixa o Executor totalmente desacoplado. Se amanhã você criar uma TaxTool, basta registrá-la:

self.tools["tax"] = TaxTool()

Nenhuma outra parte do sistema precisa ser alterada.

Observe que ele apenas registra as  ferramentas.

Não existe lógica de negócio aqui.

Depois, haverá um método semelhante a:

execute(state)

que fará aproximadamente isto:

ler do estado qual ferramenta deve executar;
procurar essa ferramenta no dicionário;
executar;
salvar o resultado novamente no estado;
devolver o estado atualizado.

Esse será o primeiro nó "genérico" do grafo."""