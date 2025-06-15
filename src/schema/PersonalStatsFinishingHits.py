import typing

from ..base_schema import BaseSchema


class PersonalStatsFinishingHits(BaseSchema):

    finishing_hits: typing.TypedDict(
        "",
        {
            "temporary": int,
            "sub_machine_guns": int,
            "slashing": int,
            "shotguns": int,
            "rifles": int,
            "pistols": int,
            "piercing": int,
            "mechanical": int,
            "machine_guns": int,
            "heavy_artillery": int,
            "hand_to_hand": int,
            "clubbing": int,
        },
    )
