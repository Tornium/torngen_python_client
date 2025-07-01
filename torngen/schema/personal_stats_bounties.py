import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class PersonalStatsBounties(BaseSchema):
    """
    JSON object of `PersonalStatsBounties`.
    """

    bounties: typing.TypedDict(
        "",
        {
            "received": typing.TypedDict("", {"value": int, "amount": int}),
            "placed": typing.TypedDict("", {"value": int, "amount": int}),
            "collected": typing.TypedDict("", {"value": int, "amount": int}),
        },
    )

    @staticmethod
    def parse(data):
        return PersonalStatsBounties(
            bounties=BaseSchema.parse(
                data.get("bounties"),
                typing.TypedDict(
                    "",
                    {
                        "received": typing.TypedDict("", {"value": int, "amount": int}),
                        "placed": typing.TypedDict("", {"value": int, "amount": int}),
                        "collected": typing.TypedDict(
                            "", {"value": int, "amount": int}
                        ),
                    },
                ),
            ),
        )
