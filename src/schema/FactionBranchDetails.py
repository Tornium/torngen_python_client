import typing

from FactionUpgradeDetails import FactionUpgradeDetails

from ..base_schema import BaseSchema


class FactionBranchDetails(BaseSchema):

    upgrades: typing.List[FactionUpgradeDetails]
    order: int
    name: str
    multiplier: int
