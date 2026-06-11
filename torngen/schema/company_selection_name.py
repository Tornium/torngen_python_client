import typing

CompanySelectionName = (
    str
    | typing.Literal[
        "applications",
        "companies",
        "employees",
        "lookup",
        "news",
        "profile",
        "snapshot",
        "stock",
        "timestamp",
    ]
)
