# Arquitetura_IA_MultiAgente
Até o momento, isso construido:
Infraestrutura ✅
✅ React + Vite
✅ Backend Python
✅ Ambiente virtual
✅ Requirements

Arquitetura Cognitiva ✅
✅ State
✅ Field Catalog
✅ Workflow
✅ Registry
✅ Planner

LangGraph ✅
✅ Primeiro grafo funcionando
✅ Primeiro Node (Planner)

Nodes ✅
✅ Atendimento
✅ Monitor

Tools
✅ ClinicalHourTool
✅ DirectCostTool
✅ CorrectedCostTool
✅ MarketTool
✅ DecisionTool
⏳ ReportTool

Entregas
✅ Passo 1 — Integrar o Planner ao StateGraph.
✅ Passo 2 — Criar o ExecutorNode.
método público chamado run(state) com uma assinatura consistente: execute(), invoke()
Não devemos adaptar o Executor às Tools; devemos padronizar as Tools.
Esse é exatamente um dos objetivos da Sprint 2: criar um contrato único entre o LangGraph e todas as ferramentas.
✅ Passo 3 — Integrar as Tools existentes ao ExecutorNode.
✅ Passo 4 — Atualizar automaticamente o State.
✅ Passo 5 — Criar o ValidatorNode.

Os antigos Passo 6/7/8 (conditional edges, Planner decidindo a próxima
etapa, graph.invoke completo) foram detalhados abaixo, em Sprint 4 —
antes deles, apareceram inconsistências que precisam ser corrigidas
primeiro (Sprint 2 e Sprint 3).

Sprint 2 — Consistência do Contrato
✅ Passo 6a — Unificar os nomes das Tools entre WORKFLOW["tool"] e as
chaves do dicionário em ExecutorNode (removido o sufixo "_tool").
✅ Fix (achado ao testar o 6a) — ExecutorNode importava o módulo de cada
Tool com "import tools.x as NomeDaClasse" em vez de importar a classe
("from tools.x import NomeDaClasse"). Isso fazia ExecutorNode() nunca
conseguir instanciar ("'module' object is not callable"). Corrigido nas
6 linhas de import do topo do executor.py.
✅ Passo 6b — Corrigir o campo "output" de cada etapa do WORKFLOW pra
bater com o atributo real que a Tool escreve no State (procedure→direct_cost,
incidence→suggested_price, market→market_average, strategy→decision).
✅ Passo 6c — Declarar validation_errors 
resolve o crash do ValidatorNode 
✅ Passo 6d — Ligar o ExecutorNode ao Registry em vez de instanciar as
Tools direto (registro centralizado em core/registry/bootstrap.py).

Sprint 3 — Tratamento de Erro
✅ Passo 7a — Padronizar validação de pré-condição em todas as Tools,
via helper compartilhado tools/validation.py (require + ToolValidationError).
⏳ Passo 7b — Definir um formato único de erro no State (ex: status +
mensagem), usado por toda Tool e todo Node.
⏳ Passo 7c — Fazer o ExecutorNode capturar exceção das Tools (try/except)
e traduzir pro formato padronizado.
⏳ Passo 7d — Definir a regra: quando o Validator encontra erro, o que
acontece (interrompe, volta uma etapa, ou pede nova pergunta).

Sprint 4 — Orquestração Real
⏳ Passo 8 — Registrar Executor, Validator, Atendimento e Monitor como
nodes reais no graph.py (hoje só existe o node "planner" indo direto pro END).
⏳ Passo 9 — Criar as conditional_edges, usando o status de erro
padronizado (Sprint 3) e o "dados suficientes?" do Planner.
⏳ Passo 10 — Planner decide dinamicamente a próxima etapa, conectando
Planner.advance()/get_tool() ao grafo.
⏳ Passo 11 — Testar o fluxo completo com graph.invoke(state) até o END
de verdade.