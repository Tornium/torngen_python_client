import typing

RacingSelectionName = (
    str
    | typing.Literal[
        "cars",
        "carupgrades",
        "lookup",
        "race",
        "races",
        "records",
        "timestamp",
        "tracks",
    ]
)
