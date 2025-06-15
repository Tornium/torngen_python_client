import typing

from UserId import UserId

from ..base_schema import BaseSchema


class FactionBalance(BaseSchema):

    members: typing.List[
        typing.TypedDict(
            "", {"username": str, "points": int, "money": int, "id": UserId}
        )
    ]
    faction: typing.TypedDict("", {"scope": int, "points": int, "money": int})
