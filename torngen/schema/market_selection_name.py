import typing

MarketSelectionName = (
    str
    | typing.Literal[
        "auctionhouse",
        "auctionhouselisting",
        "bazaar",
        "itemmarket",
        "pointsmarket",
        "properties",
        "rentals",
        "lookup",
        "timestamp",
    ]
)
