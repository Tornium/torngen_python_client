import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_oc_history_role import FactionOcHistoryRole


@dataclass
class FactionOcHistoryRoleDetails(BaseSchema):
    """
    JSON object of `FactionOcHistoryRoleDetails`.
    """

    role: FactionOcHistoryRole

    @staticmethod
    def parse(data):
        return FactionOcHistoryRoleDetails(
            role=BaseSchema.parse(data.get("role"), FactionOcHistoryRole),
        )
