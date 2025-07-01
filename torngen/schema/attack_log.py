import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .attack_action_enum import AttackActionEnum
from .item_id import ItemId
from .user_id import UserId


@dataclass
class AttackLog(BaseSchema):
    """
    JSON object of `AttackLog`.
    """

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

    @staticmethod
    def parse(data):
        return AttackLog(
            timestamp=BaseSchema.parse(data.get("timestamp"), int),
            text=BaseSchema.parse(data.get("text"), str),
            icon=BaseSchema.parse(data.get("icon"), str),
            defender=BaseSchema.parse(
                data.get("defender"),
                None | typing.TypedDict("", {"name": str, "id": UserId}),
            ),
            attacker_item=BaseSchema.parse(
                data.get("attacker_item"),
                typing.TypedDict("", {"name": str, "id": ItemId}),
            ),
            attacker=BaseSchema.parse(
                data.get("attacker"),
                None
                | typing.TypedDict(
                    "",
                    {
                        "name": str,
                        "item": None
                        | typing.TypedDict("", {"name": str, "id": ItemId}),
                        "id": UserId,
                    },
                ),
            ),
            action=BaseSchema.parse(data.get("action"), AttackActionEnum),
        )
