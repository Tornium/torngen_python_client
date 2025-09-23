import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_branch_id import FactionBranchId


@dataclass
class FactionUpgradeDetails(BaseSchema):
    """
    JSON object of `FactionUpgradeDetails`.
    """

    unlocked_at: typing.Optional[int]
    name: str
    level: int
    id: FactionBranchId
    cost: int
    ability: str

    @staticmethod
    def parse(data):
        return FactionUpgradeDetails(
            unlocked_at=BaseSchema.parse(data.get("unlocked_at"), typing.Optional[int]),
            name=BaseSchema.parse(data.get("name"), str),
            level=BaseSchema.parse(data.get("level"), int),
            id=BaseSchema.parse(data.get("id"), FactionBranchId),
            cost=BaseSchema.parse(data.get("cost"), int),
            ability=BaseSchema.parse(data.get("ability"), str),
        )
