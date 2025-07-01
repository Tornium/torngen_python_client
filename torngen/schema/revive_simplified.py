import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_id import FactionId
from .revive_id import ReviveId
from .user_id import UserId


@dataclass
class ReviveSimplified(BaseSchema):
    """
    JSON object of `ReviveSimplified`.
    """

    timestamp: int
    target: typing.TypedDict(
        "",
        {
            "online_status": str,
            "last_action": int,
            "id": UserId,
            "hospital_reason": str,
            "faction_id": None | FactionId,
            "early_discharge": bool,
        },
    )
    success_chance: int | float
    reviver: typing.TypedDict("", {"id": UserId, "faction_id": None | FactionId})
    result: str
    id: ReviveId

    @staticmethod
    def parse(data):
        return ReviveSimplified(
            timestamp=BaseSchema.parse(data.get("timestamp"), int),
            target=BaseSchema.parse(
                data.get("target"),
                typing.TypedDict(
                    "",
                    {
                        "online_status": str,
                        "last_action": int,
                        "id": UserId,
                        "hospital_reason": str,
                        "faction_id": None | FactionId,
                        "early_discharge": bool,
                    },
                ),
            ),
            success_chance=BaseSchema.parse(data.get("success_chance"), int | float),
            reviver=BaseSchema.parse(
                data.get("reviver"),
                typing.TypedDict("", {"id": UserId, "faction_id": None | FactionId}),
            ),
            result=BaseSchema.parse(data.get("result"), str),
            id=BaseSchema.parse(data.get("id"), ReviveId),
        )
