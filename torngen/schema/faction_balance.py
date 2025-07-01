import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_id import UserId


@dataclass
class FactionBalance(BaseSchema):
    """
    JSON object of `FactionBalance`.
    """

    members: typing.List[
        typing.TypedDict(
            "", {"username": str, "points": int, "money": int, "id": UserId}
        )
    ]
    faction: typing.TypedDict("", {"scope": int, "points": int, "money": int})

    @staticmethod
    def parse(data):
        return FactionBalance(
            members=BaseSchema.parse(
                data.get("members"),
                typing.List[
                    typing.TypedDict(
                        "", {"username": str, "points": int, "money": int, "id": UserId}
                    )
                ],
            ),
            faction=BaseSchema.parse(
                data.get("faction"),
                typing.TypedDict("", {"scope": int, "points": int, "money": int}),
            ),
        )
