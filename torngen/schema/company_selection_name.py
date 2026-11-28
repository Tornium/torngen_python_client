import typing

CompanySelectionName = (
    str
    | typing.Literal[
        "applications",
        "companies",
        "employees",
        "news",
        "profile",
        "stock",
        "lookup",
        "timestamp",
    ]
)
