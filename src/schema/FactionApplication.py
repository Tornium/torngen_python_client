import typing

from FactionApplicationStatusEnum import FactionApplicationStatusEnum
from UserId import UserId

from ..base_schema import BaseSchema


class FactionApplication(BaseSchema):

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
