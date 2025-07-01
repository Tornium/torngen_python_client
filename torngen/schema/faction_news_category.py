from ..base_schema import BaseSchema


class FactionNewsCategory(BaseSchema):

    values = [
        "main",
        "attack",
        "armoryDeposit",
        "armoryAction",
        "territoryWar",
        "rankedWar",
        "territoryGain",
        "chain",
        "crime",
        "membership",
        "depositFunds",
        "giveFunds",
    ]
