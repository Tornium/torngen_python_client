import typing

from FactionId import FactionId
from ReviveId import ReviveId
from UserId import UserId

from ..base_schema import BaseSchema


class ReviveSimplified(BaseSchema):

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
