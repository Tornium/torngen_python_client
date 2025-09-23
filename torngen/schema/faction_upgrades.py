import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_branch_details import FactionBranchDetails
from .faction_upgrade_details import FactionUpgradeDetails


@dataclass
class FactionUpgrades(BaseSchema):
    """
    JSON object of `FactionUpgrades`.
    """

    war: typing.List[FactionBranchDetails]
    peace: typing.List[FactionBranchDetails]
    core: typing.TypedDict(
        "", {"upgrades": typing.Optional[typing.List[FactionUpgradeDetails]]}
    )

    @staticmethod
    def parse(data):
        return FactionUpgrades(
            war=BaseSchema.parse(data.get("war"), typing.List[FactionBranchDetails]),
            peace=BaseSchema.parse(
                data.get("peace"), typing.List[FactionBranchDetails]
            ),
            core=BaseSchema.parse(
                data.get("core"),
                typing.TypedDict(
                    "",
                    {"upgrades": typing.Optional[typing.List[FactionUpgradeDetails]]},
                ),
            ),
        )
