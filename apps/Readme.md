Objetivo: Criar o State (memória compartilhada do LangGraph).
apps/backend/core/state/
models.py
schemas.py
constants.py
__init__.py

Objetivo: Criar o Field Catalog. Ele será consultado por:
Planner
Atendimento
Validator
Workflow

Estrutura: registry - Resultado: Agora teremos um único local para registrar tudo.

Planner Node: Ele será o primeiro Node do LangGraph e será responsável por responder apenas:
Qual etapa está ativa?
Quais campos faltam?
Posso executar a Tool?
Qual é a próxima etapa?