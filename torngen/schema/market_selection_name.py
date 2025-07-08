import typing

MarketSelectionName = (
    str
    | typing.Literal[
        "bazaar",
        "itemmarket",
        "properties",
        "rentals",
        "lookup",
        "timestamp",
        "pointsmarket",
    ]
)
