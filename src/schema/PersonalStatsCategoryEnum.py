from ..base_schema import BaseSchema


class PersonalStatsCategoryEnum(BaseSchema):

    values = [
        "all",
        "popular",
        "attacking",
        "battle_stats",
        "jobs",
        "trading",
        "jail",
        "hospital",
        "finishing_hits",
        "communication",
        "crimes",
        "bounties",
        "investments",
        "items",
        "travel",
        "drugs",
        "missions",
        "racing",
        "networth",
        "other",
        "itemmarketcustomers",
        "itemmarketsales",
        "itemmarketrevenue",
        "itemmarketfees",
    ]
