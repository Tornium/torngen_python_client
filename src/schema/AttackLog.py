import typing

from AttackActionEnum import AttackActionEnum
from ItemId import ItemId
from UserId import UserId

from ..base_schema import BaseSchema


class AttackLog(BaseSchema):

    timestamp: int
    text: str
    icon: str
    defender: None | typing.TypedDict("", {"name": str, "id": UserId})
    attacker_item: typing.TypedDict("", {"name": str, "id": ItemId})
    attacker: None | typing.TypedDict(
        "",
        {
            "name": str,
            "item": None | typing.TypedDict("", {"name": str, "id": ItemId}),
            "id": UserId,
        },
    )
    action: AttackActionEnum
