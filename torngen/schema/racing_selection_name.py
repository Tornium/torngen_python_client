import typing

RacingSelectionName = (
    str
    | typing.Literal[
        "cars",
        "carupgrades",
        "race",
        "races",
        "records",
        "tracks",
        "lookup",
        "timestamp",
    ]
)
