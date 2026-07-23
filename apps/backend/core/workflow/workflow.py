# WORKFLOW é a fonte única de verdade do processo de precificação.
# Planner, Executor e Validator leem esta lista — nenhum deles conhece
# regra de negócio diretamente, só consultam esta configuração.
#
# Passo 6a (Sprint 2): o campo "tool" abaixo precisa usar EXATAMENTE a
# mesma chave que existe em ExecutorNode.tools (core/nodes/executor.py).
# Antes desta correção, "tool" vinha com sufixo "_tool" (ex: "clinical_hour_tool"),
# mas o dicionário do ExecutorNode usa a chave sem sufixo (ex: "clinical_hour").
# Isso ainda não quebrava nada porque nada ligava Planner -> ExecutorNode
# usando este campo, mas ia gerar KeyError assim que essa ligação fosse feita
# (Sprint 4 / conditional edges). Convenção escolhida: SEM sufixo "_tool",
# porque é o que o próprio ExecutorNode já usa (inclusive na linha comentada
# do "report"), e porque a classe já deixa claro que é uma Tool
# (ex: ClinicalHourTool) — repetir "_tool" na chave é redundante.
#
# TODO (Passo 6b): o campo "output" desta lista também está incorreto para
# a maioria das etapas — ele deveria ser o atributo do State que a Tool
# realmente escreve (ex: etapa "incidence" roda o CorrectedCostTool, que
# escreve state.suggested_price, não state.incidence). Ainda não corrigido
# aqui de propósito, é o próximo passo da sprint.
WORKFLOW = [
    {
        "step": "clinical_hour",
        "fields": [
            "working_hours",
            "fixed_costs",
            "variable_costs",
        ],
        "tool": "clinical_hour",       # antes: "clinical_hour_tool"
        "output": "clinical_hour",
        "next": "procedure",
    },
    {
        "step": "procedure",
        "fields": [
            "procedure",
            "procedure_time",
        ],
        "tool": "direct_cost",         # antes: "direct_cost_tool"
        "output": "procedure",
        "next": "incidence",
    },
    {
        "step": "incidence",
        "fields": [
            "desired_margin",
        ],
        "tool": "corrected_cost",      # antes: "corrected_cost_tool"
        "output": "incidence",
        "next": "market",
    },
    {
        "step": "market",
        "fields": [],
        "tool": "market",              # antes: "market_tool"
        "output": "market",
        "next": "strategy",
    },
    {
        "step": "strategy",
        "fields": [],
        "tool": "decision",            # antes: "decision_tool"
        "output": "strategy",
        "next": "report",
    },
    {
        "step": "report",
        "fields": [],
        "tool": "report",              # antes: "report_tool" (ReportTool ainda não existe — ver Sprint 3/ReportTool)
        "output": "report",
        "next": None,
    },
]