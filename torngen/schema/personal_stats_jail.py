import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class PersonalStatsJail(BaseSchema):
    """
    JSON object of `PersonalStatsJail`.
    """

    jail: typing.TypedDict(
        "",
        {
            "times_jailed": int,
            "busts": typing.TypedDict("", {"success": int, "fails": int}),
            "bails": typing.TypedDict("", {"fees": int, "amount": int}),
        },
    )

    @staticmethod
    def parse(data):
        return PersonalStatsJail(
            jail=BaseSchema.parse(
                data.get("jail"),
                typing.TypedDict(
                    "",
                    {
                        "times_jailed": int,
                        "busts": typing.TypedDict("", {"success": int, "fails": int}),
                        "bails": typing.TypedDict("", {"fees": int, "amount": int}),
                    },
                ),
            ),
        )
