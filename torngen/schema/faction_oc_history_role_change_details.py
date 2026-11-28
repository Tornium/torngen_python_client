import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_oc_history_role import FactionOcHistoryRole


@dataclass
class FactionOcHistoryRoleChangeDetails(BaseSchema):
    """
    JSON object of `FactionOcHistoryRoleChangeDetails`.
    """

    old_role: FactionOcHistoryRole
    new_role: FactionOcHistoryRole

    @staticmethod
    def parse(data):
        return FactionOcHistoryRoleChangeDetails(
            old_role=BaseSchema.parse(data.get("old_role"), FactionOcHistoryRole),
            new_role=BaseSchema.parse(data.get("new_role"), FactionOcHistoryRole),
        )
