import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class PersonalStatsMissions(BaseSchema):
    """
    JSON object of `PersonalStatsMissions`.
    """

    missions: typing.TypedDict(
        "",
        {
            "missions": int,
            "credits": int,
            "contracts": typing.TypedDict("", {"total": int, "duke": int}),
        },
    )

    @staticmethod
    def parse(data):
        return PersonalStatsMissions(
            missions=BaseSchema.parse(
                data.get("missions"),
                typing.TypedDict(
                    "",
                    {
                        "missions": int,
                        "credits": int,
                        "contracts": typing.TypedDict("", {"total": int, "duke": int}),
                    },
                ),
            ),
        )
