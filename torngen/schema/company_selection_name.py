import typing

CompanySelectionName = (
    str
    | typing.Literal[
        "applications",
        "employees",
        "lookup",
        "profile",
        "stock",
        "timestamp",
        "companies",
        "news",
        "search",
    ]
)
