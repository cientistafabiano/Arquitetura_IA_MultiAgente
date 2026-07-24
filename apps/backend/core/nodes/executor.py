"""Objetivo: Criar o primeiro nó inteligente do workflow: ExecutorNode.

A responsabilidade dele será:

receber o nome da ferramenta que deve ser executada;
localizar a classe correspondente;
executar a ferramenta;
devolver o resultado para o estado do LangGraph.

Assim, nenhum outro componente precisará conhecer as ferramentas diretamente.

Passo 6d (Sprint 2): antes, o ExecutorNode importava e instanciava cada
Tool direto, num dicionário fixo dentro do __init__. Agora ele só conhece
o Registry — quem registra as Tools é core/registry/bootstrap.py.

Passo 7c (Sprint 3): antes, se uma Tool levantasse ToolValidationError
(Passo 7a), o erro subia cru e quebrava o grafo inteiro. Agora o
ExecutorNode captura especificamente ToolValidationError e traduz pro
formato padronizado do State (Passo 7b: state.mark_error()). Erros
inesperados (bugs de verdade, não falta de dado) continuam subindo cru
de propósito — não queremos esconder um bug atrás de um "status: error"
genérico que o grafo vai tratar como "faltou informação do usuário".

"""
from core.registry import registry
from core.registry.bootstrap import register_tools
from tools.validation import ToolValidationError

# Garante que as Tools estão registradas antes de qualquer execução.
# Registrar de novo é inofensivo (só sobrescreve com a mesma instância),
# então importar este módulo mais de uma vez é seguro.
#
# Nota: isso é um efeito colateral no import, meio implícito — pragmático
# pra este estágio do projeto (ainda não existe uma rotina de startup).
# Quando a API (FastAPI) entrar, vale mover isso pra um hook de startup
# explícito em vez de rodar no import.
register_tools()

class ExecutorNode:

    def execute(self, state):

        tool = registry.get_tool(state.next_step)

        if tool is None:
            # Bug de configuração (WORKFLOW aponta pra uma tool que
            # ninguém registrou) — não é "faltou dado do usuário", é erro
            # de quem está desenvolvendo. Fica explícito, não vira
            # state.mark_error().
            raise ValueError(
                f"Tool '{state.next_step}' não está registrada no Registry. "
                f"Verifique core/registry/bootstrap.py."
            )

        try:
            return tool.execute(state)
        except ToolValidationError as erro:
            return state.mark_error(str(erro))


"""class ExecutorNode:

    def execute(self, state):

        tool = registry.get_tool(state.next_step)

        if tool is None:
            raise ValueError(
                f"Tool '{state.next_step}' não está registrada no Registry. "
                f"Verifique core/registry/bootstrap.py."
            )

        return tool.execute(state)


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