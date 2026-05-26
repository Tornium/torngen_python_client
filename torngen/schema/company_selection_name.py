import typing

CompanySelectionName = (
    str
    | typing.Literal[
        "applications",
        "employees",
        "lookup",
        "news",
        "profile",
        "stock",
        "timestamp",
        "companies",
        "search",
    ]
)
