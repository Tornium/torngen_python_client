import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_id import FactionId
from .revive_id import ReviveId
from .user_id import UserId


@dataclass
class Revive(BaseSchema):
    """
    JSON object of `Revive`.
    """

    timestamp: int
    target: typing.TypedDict(
        "",
        {
            "online_status": str,
            "name": str,
            "last_action": int,
            "id": UserId,
            "hospital_reason": str,
            "faction": None | typing.TypedDict("", {"name": str, "id": FactionId}),
            "early_discharge": bool,
        },
    )
    success_chance: int | float
    reviver: typing.TypedDict(
        "",
        {
            "skill": None | int | float,
            "name": str,
            "id": UserId,
            "faction": None | typing.TypedDict("", {"name": str, "id": FactionId}),
        },
    )
    result: str
    id: ReviveId

    @staticmethod
    def parse(data):
        return Revive(
            timestamp=BaseSchema.parse(data.get("timestamp"), int),
            target=BaseSchema.parse(
                data.get("target"),
                typing.TypedDict(
                    "",
                    {
                        "online_status": str,
                        "name": str,
                        "last_action": int,
                        "id": UserId,
                        "hospital_reason": str,
                        "faction": None
                        | typing.TypedDict("", {"name": str, "id": FactionId}),
                        "early_discharge": bool,
                    },
                ),
            ),
            success_chance=BaseSchema.parse(data.get("success_chance"), int | float),
            reviver=BaseSchema.parse(
                data.get("reviver"),
                typing.TypedDict(
                    "",
                    {
                        "skill": None | int | float,
                        "name": str,
                        "id": UserId,
                        "faction": None
                        | typing.TypedDict("", {"name": str, "id": FactionId}),
                    },
                ),
            ),
            result=BaseSchema.parse(data.get("result"), str),
            id=BaseSchema.parse(data.get("id"), ReviveId),
        )
