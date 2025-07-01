import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class PersonalStatsFinishingHits(BaseSchema):
    """
    JSON object of `PersonalStatsFinishingHits`.
    """

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

    @staticmethod
    def parse(data):
        return PersonalStatsFinishingHits(
            finishing_hits=BaseSchema.parse(
                data.get("finishing_hits"),
                typing.TypedDict(
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
                ),
            ),
        )
