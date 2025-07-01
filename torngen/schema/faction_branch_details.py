import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_upgrade_details import FactionUpgradeDetails


@dataclass
class FactionBranchDetails(BaseSchema):
    """
    JSON object of `FactionBranchDetails`.
    """

    upgrades: typing.List[FactionUpgradeDetails]
    order: int
    name: str
    multiplier: int

    @staticmethod
    def parse(data):
        return FactionBranchDetails(
            upgrades=BaseSchema.parse(
                data.get("upgrades"), typing.List[FactionUpgradeDetails]
            ),
            order=BaseSchema.parse(data.get("order"), int),
            name=BaseSchema.parse(data.get("name"), str),
            multiplier=BaseSchema.parse(data.get("multiplier"), int),
        )
