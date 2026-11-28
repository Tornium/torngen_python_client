import typing

MarketSelectionName = (
    str
    | typing.Literal[
        "auctionhouse",
        "auctionhouselisting",
        "bazaar",
        "itemhistory",
        "itemmarket",
        "pointshistory",
        "pointsmarket",
        "properties",
        "rentals",
        "lookup",
        "timestamp",
    ]
)
