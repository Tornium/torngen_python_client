import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_branch_state_enum import FactionBranchStateEnum
from .faction_upgrades import FactionUpgrades


@dataclass
class FactionUpgradesResponse(BaseSchema):
    """
    JSON object of `FactionUpgradesResponse`.
    """

    upgrades: FactionUpgrades
    state: FactionBranchStateEnum

    @staticmethod
    def parse(data):
        return FactionUpgradesResponse(
            upgrades=BaseSchema.parse(data.get("upgrades"), FactionUpgrades),
            state=BaseSchema.parse(data.get("state"), FactionBranchStateEnum),
        )
