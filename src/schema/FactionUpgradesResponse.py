import typing

from FactionBranchStateEnum import FactionBranchStateEnum
from FactionUpgrades import FactionUpgrades

from ..base_schema import BaseSchema


class FactionUpgradesResponse(BaseSchema):

    upgrades: FactionUpgrades
    state: FactionBranchStateEnum
