import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_branch_id import FactionBranchId
from .faction_stat_enum import FactionStatEnum


@dataclass
class TornFactionTreeBranch(BaseSchema):
    """
    JSON object of `TornFactionTreeBranch`.
    """

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

    @staticmethod
    def parse(data):
        return TornFactionTreeBranch(
            upgrades=BaseSchema.parse(
                data.get("upgrades"),
                typing.List[
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
                ],
            ),
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), FactionBranchId),
        )
