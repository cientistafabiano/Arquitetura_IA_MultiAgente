from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class SoberanaState(BaseModel):
    # Conversa
    messages: List[Dict[str, Any]] = Field(default_factory=list)
    current_step: str = "clinical_hour"
    next_step: Optional[str] = None
    status: str = "started"

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

    # Mercado
    market_average: Optional[float] = None

    # Resultado
    recommendations: List[str] = Field(default_factory=list)