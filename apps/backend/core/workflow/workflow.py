WORKFLOW = [
    {
        "step": "clinical_hour",
        "fields": [
            "working_hours",
            "fixed_costs",
            "variable_costs",
        ],
        "tool": "clinical_hour_tool",
        "next": "procedure",
    },
    {
        "step": "procedure",
        "fields": [
            "procedure",
            "procedure_time",
        ],
        "tool": "direct_cost_tool",
        "next": "incidence",
    },
    {
        "step": "incidence",
        "fields": [
            "desired_margin",
        ],
        "tool": "corrected_cost_tool",
        "next": "market",
    },
    {
        "step": "market",
        "fields": [],
        "tool": "market_tool",
        "next": "strategy",
    },
    {
        "step": "strategy",
        "fields": [],
        "tool": "decision_tool",
        "next": "report",
    },
    {
        "step": "report",
        "fields": [],
        "tool": "report_tool",
        "next": None,
    },
]