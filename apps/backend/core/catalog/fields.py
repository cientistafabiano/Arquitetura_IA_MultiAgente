FIELDS = {
    "working_hours": {
        "question": "Quantas horas produtivas sua clínica possui por mês?",
        "unit": "horas",
        "example": "160",
        "type": "float",
        "required": True,
    },

    "fixed_costs": {
        "question": "Qual o valor dos custos fixos mensais?",
        "unit": "R$",
        "example": "12000",
        "type": "float",
        "required": True,
    },

    "variable_costs": {
        "question": "Qual o valor dos custos variáveis mensais?",
        "unit": "R$",
        "example": "3500",
        "type": "float",
        "required": True,
    },

    "desired_margin": {
        "question": "Qual a margem de lucro desejada?",
        "unit": "%",
        "example": "30",
        "type": "float",
        "required": True,
    },
}