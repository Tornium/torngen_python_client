import typing

from FactionBranchId import FactionBranchId

from ..base_schema import BaseSchema


class FactionUpgradeDetails(BaseSchema):

    unlocked_at: int
    name: str
    level: int
    id: FactionBranchId
    cost: int
    ability: str
