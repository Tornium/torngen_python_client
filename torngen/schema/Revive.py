import typing

from FactionId import FactionId
from ReviveId import ReviveId
from UserId import UserId

from ..base_schema import BaseSchema


class Revive(BaseSchema):

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
