import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .basic_user import BasicUser
from .faction_oc_history_action_enum import FactionOcHistoryActionEnum
from .faction_oc_history_injury_details import FactionOcHistoryInjuryDetails
from .faction_oc_history_item import FactionOcHistoryItem
from .faction_oc_history_payout_details import FactionOcHistoryPayoutDetails
from .faction_oc_history_payout_received_details import (
    FactionOcHistoryPayoutReceivedDetails,
)
from .faction_oc_history_punishment_details import FactionOcHistoryPunishmentDetails
from .faction_oc_history_role_change_details import FactionOcHistoryRoleChangeDetails
from .faction_oc_history_role_details import FactionOcHistoryRoleDetails
from .faction_oc_history_spawn_details import FactionOcHistorySpawnDetails


@dataclass
class FactionOcHistoryEntry(BaseSchema):
    """
    JSON object of `FactionOcHistoryEntry`.
    """

    user: None | BasicUser
    timestamp: int
    text: str
    performed_by: None | BasicUser
    id: int
    details: (
        None
        | FactionOcHistoryPayoutReceivedDetails
        | FactionOcHistoryPayoutDetails
        | FactionOcHistoryInjuryDetails
        | FactionOcHistoryPunishmentDetails
        | FactionOcHistoryItem
        | FactionOcHistorySpawnDetails
        | FactionOcHistoryRoleChangeDetails
        | FactionOcHistoryRoleDetails
    )
    action: FactionOcHistoryActionEnum

    @staticmethod
    def parse(data):
        return FactionOcHistoryEntry(
            user=BaseSchema.parse(data.get("user"), None | BasicUser),
            timestamp=BaseSchema.parse(data.get("timestamp"), int),
            text=BaseSchema.parse(data.get("text"), str),
            performed_by=BaseSchema.parse(data.get("performed_by"), None | BasicUser),
            id=BaseSchema.parse(data.get("id"), int),
            details=BaseSchema.parse(
                data.get("details"),
                None
                | FactionOcHistoryPayoutReceivedDetails
                | FactionOcHistoryPayoutDetails
                | FactionOcHistoryInjuryDetails
                | FactionOcHistoryPunishmentDetails
                | FactionOcHistoryItem
                | FactionOcHistorySpawnDetails
                | FactionOcHistoryRoleChangeDetails
                | FactionOcHistoryRoleDetails,
            ),
            action=BaseSchema.parse(data.get("action"), FactionOcHistoryActionEnum),
        )
