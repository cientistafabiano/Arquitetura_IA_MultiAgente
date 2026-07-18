"""Sua única responsabilidade será verificar se a Tool executou corretamente.
Adicionar a chave "output" em todas as etapas do WORKFLOW.
Fazer o ValidatorNode utilizar apenas o WORKFLOW

Se amanhã você criar: ProfitProjectionTool

basta adicionar ao WORKFLOW:

{
    "step": "profit_projection",
    "tool": "profit_projection",
    "output": "profit_projection",
    ...
}

O Validator continuará funcionando sem nenhuma alteração.

Esse é um dos princípios que estamos buscando: os nós do LangGraph não dependem das regras de negócio, apenas da configuração do fluxo."""

from core.workflow import WORKFLOW


class ValidatorNode:

    def get_current_step(self, state):
        """
        Localiza a configuração da etapa atual no WORKFLOW.
        """

        for step in WORKFLOW:
            if step["step"] == state.current_step:
                return step

        return None


    def execute(self, state):
        """
        Valida se a Tool produziu o resultado esperado.
        """

        state.validation_errors = []

        step = self.get_current_step(state)

        if step is None:
            state.validation_errors.append(
                "Etapa inexistente."
            )
            return state

        output = step["output"]

        if getattr(state, output, None) is None:
            state.validation_errors.append(
                f"{output} não foi produzido."
            )

        return state


"""Componente	Responsabilidade
Planner	         Decide a próxima ação
Executor	       Executa a Tool escolhida
Tool	         Altera o estado
Validator	      Verifica se o estado ficou consistente

Cada componente faz uma única coisa, o que segue o princípio da responsabilidade única (SRP).

Observe o que estamos construindo:

Planner consulta o WORKFLOW.
Executor consulta o WORKFLOW (indiretamente, via Planner).
Validator consulta o WORKFLOW.

O WORKFLOW passa a ser a fonte única da verdade

Isso significa que, para adicionar uma nova etapa ao sistema, você precisará apenas:

Criar a Tool.
Adicionar a etapa ao WORKFLOW.

Nem o Planner, nem o Executor, nem o Validator precisarão ser modificados."""
