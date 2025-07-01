import typing

from FactionBranchDetails import FactionBranchDetails
from FactionUpgradeDetails import FactionUpgradeDetails

from ..base_schema import BaseSchema


class FactionUpgrades(BaseSchema):

    war: typing.List[FactionBranchDetails]
    peace: typing.List[FactionBranchDetails]
    core: typing.TypedDict("", {"upgrades": typing.List[FactionUpgradeDetails]})
