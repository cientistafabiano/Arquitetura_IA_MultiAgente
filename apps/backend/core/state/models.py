from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class SoberanaState(BaseModel):
    # Conversa
    messages: List[Dict[str, Any]] = Field(default_factory=list)
    current_step: str = "clinical_hour"
    next_step: Optional[str] = None
     # Passo 7b (Sprint 3): "status" já existia mas ninguém usava. Agora
    # tem semântica definida: "in_progress" (fluxo normal) ou "error"
    # (algo falhou). error_message guarda a mensagem legível quando
    # status == "error". Nenhum código antigo dependia do valor default
    # anterior ("started"), então trocar é seguro.
    status: str = "in_progress"
    error_message: Optional[str] = None

    # Clínica
    clinic_name: Optional[str] = None
    professional_name: Optional[str] = None

    # Procedimento
    procedure: Optional[str] = None
    procedure_time: Optional[int] = None

    # Financeiro
    fixed_costs: Optional[float] = None
    variable_costs: Optional[float] = None
    working_hours: Optional[float] = None
    desired_margin: Optional[float] = None
    suggested_price: Optional[float] = None
    ##depois q criamos o arquivo clinical_hour_tool.py, podemos adicionar o campo clinical_hour no estado, para armazenar o resultado do calculo da hora clinica
    clinical_hour: float | None = None
    ##depois q criamos o arquivo direct_cost_tool.py, podemos adicionar o campo direct_cost no estado, para armazenar o resultado do calculo do custo direto
    direct_cost: float | None = None
    # Mercado
    market_average: Optional[float] = None
    #decisao
    decision: str | None = None

    # Resultado
    recommendations: List[str] = Field(default_factory=list)

    # Passo 6c (Sprint 2): campo que o ValidatorNode usa pra acumular
    # mensagens de erro de validação. Antes não existia no schema, e o
    # ValidatorNode.execute() quebrava ao tentar atribuir um campo que o
    # Pydantic não conhecia ("no field validation_errors").
    validation_errors: List[str] = Field(default_factory=list)

    # Passo 7b (Sprint 3): forma única de qualquer Tool/Node sinalizar
    # erro no State. Em vez de cada um escrever status/error_message na
    # mão (e arriscar formatos diferentes), todos chamam este método.
    def mark_error(self, message: str) -> "SoberanaState":
        self.status = "error"
        self.error_message = message
        return self

    @property
    def has_error(self) -> bool:
        return self.status == "error"