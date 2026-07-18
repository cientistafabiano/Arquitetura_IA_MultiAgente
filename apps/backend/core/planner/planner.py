"""Planner deve fazer:

✅ sabe em qual etapa está (current_step);
✅ conhece o WORKFLOW;
✅ verifica campos obrigatórios;
✅ decide se pode executar a Tool;
✅ sabe qual Tool pertence à etapa;
✅ sabe qual é a próxima etapa."""


from core.workflow import WORKFLOW
from core.catalog import FIELDS

class Planner:

    def get_current_step(self, state):
        for step in WORKFLOW:
            if step["step"] == state.current_step:
                return step
        return None

    def get_missing_fields(self, state):
        step = self.get_current_step(state)

        missing = []

        for field in step["fields"]:
            if getattr(state, field, None) is None:
                missing.append(field)

        return missing

    def can_execute(self, state):
        return len(self.get_missing_fields(state)) == 0

    def next_step(self, state):
        step = self.get_current_step(state)
        return step["next"]
    
    ##atualização
    """Agora o Planner deixará de apenas listar campos faltantes.
    Ele passará a decidir automaticamente:
    ainda falta informação → Atendimento;
    todos os campos preenchidos → Tool;
    Tool terminou → próxima etapa.
    Esse será o momento em que o LangGraph começará a mostrar seu verdadeiro potencial."""
    
    def should_execute_tool(self, state):
        return self.can_execute(state)

    def get_tool(self, state):
        step = self.get_current_step(state)
        return step["tool"]


    def advance(self, state):
        state.current_step = self.next_step(state)
        return state