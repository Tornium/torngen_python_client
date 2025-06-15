from ..base_schema import BaseSchema


class FactionAttackResult(BaseSchema):

    values = [
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
