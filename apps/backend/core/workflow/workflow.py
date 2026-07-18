WORKFLOW = [
    {
        "step": "clinical_hour",
        "fields": [
            "working_hours",
            "fixed_costs",
            "variable_costs",
        ],
        "tool": "clinical_hour_tool",
        "output": "clinical_hour",
        "next": "procedure",
    },
    {
        "step": "procedure",
        "fields": [
            "procedure",
            "procedure_time",
        ],
        "tool": "direct_cost_tool",
        "output": "procedure",
        "next": "incidence",
    },
    {
        "step": "incidence",
        "fields": [
            "desired_margin",
        ],
        "tool": "corrected_cost_tool",
        "output": "incidence",
        "next": "market",
    },
    {
        "step": "market",
        "fields": [],
        "tool": "market_tool",
        "output": "market",
        "next": "strategy",
    },
    {
        "step": "strategy",
        "fields": [],
        "tool": "decision_tool",
        "output": "strategy",
        "next": "report",
    },
    {
        "step": "report",
        "fields": [],
        "tool": "report_tool",
        "output": "report",
        "next": None,
    },
]