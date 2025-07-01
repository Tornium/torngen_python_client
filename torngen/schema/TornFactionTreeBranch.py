import typing

from FactionBranchId import FactionBranchId
from FactionStatEnum import FactionStatEnum

from ..base_schema import BaseSchema


class TornFactionTreeBranch(BaseSchema):

    upgrades: typing.List[
        typing.TypedDict(
            "",
            {
                "name": str,
                "level": int,
                "cost": int,
                "challenge": None
                | typing.TypedDict(
                    "",
                    {
                        "stat": FactionStatEnum,
                        "description": str,
                        "amount_required": int,
                    },
                ),
                "ability": str,
            },
        )
    ]
    name: str
    id: FactionBranchId
