import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_application_status_enum import FactionApplicationStatusEnum
from .user_id import UserId


@dataclass
class FactionApplication(BaseSchema):
    """
    JSON object of `FactionApplication`.
    """

    valid_until: int
    user: typing.TypedDict(
        "",
        {
            "stats": typing.TypedDict(
                "", {"strength": int, "speed": int, "dexterity": int, "defense": int}
            ),
            "name": str,
            "level": int,
            "id": UserId,
        },
    )
    status: FactionApplicationStatusEnum
    message: str
    id: int

    @staticmethod
    def parse(data):
        return FactionApplication(
            valid_until=BaseSchema.parse(data.get("valid_until"), int),
            user=BaseSchema.parse(
                data.get("user"),
                typing.TypedDict(
                    "",
                    {
                        "stats": typing.TypedDict(
                            "",
                            {
                                "strength": int,
                                "speed": int,
                                "dexterity": int,
                                "defense": int,
                            },
                        ),
                        "name": str,
                        "level": int,
                        "id": UserId,
                    },
                ),
            ),
            status=BaseSchema.parse(data.get("status"), FactionApplicationStatusEnum),
            message=BaseSchema.parse(data.get("message"), str),
            id=BaseSchema.parse(data.get("id"), int),
        )
