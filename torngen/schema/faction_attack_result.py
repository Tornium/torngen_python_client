import typing

FactionAttackResult = typing.Literal[
    "None",
    "Attacked",
    "Mugged",
    "Hospitalized",
    "Arrested",
    "Looted",
    "Lost",
    "Stalemate",
    "Assist",
    "Escape",
    "Timeout",
    "Special",
    "Bounty",
    "Interrupted",
]
