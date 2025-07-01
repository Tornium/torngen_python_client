from ..base_schema import BaseSchema


class FactionRankEnum(BaseSchema):

    values = [
        "Unranked",
        "Bronze",
        "Silver",
        "Gold",
        "Platinum",
        "Diamond",
    ]
