import typing

from ..base_schema import BaseSchema


class PersonalStatsTravel(BaseSchema):

    travel: typing.TypedDict(
        "",
        {
            "united_kingdom": int,
            "united_arab_emirates": int,
            "total": int,
            "time_spent": int,
            "switzerland": int,
            "south_africa": int,
            "mexico": int,
            "japan": int,
            "items_bought": int,
            "hunting": typing.TypedDict("", {"skill": int}),
            "hawaii": int,
            "defends_lost": int,
            "china": int,
            "cayman_islands": int,
            "canada": int,
            "attacks_won": int,
            "argentina": int,
        },
    )
