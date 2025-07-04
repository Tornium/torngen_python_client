import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_organized_crime_payout_type import FactionOrganizedCrimePayoutType
from .user_id import UserId


@dataclass
class FactionCrimeRewardPayout(BaseSchema):
    """
    JSON object of `FactionCrimeRewardPayout`.
    """

    type: FactionOrganizedCrimePayoutType
    percentage: int
    paid_by: UserId
    paid_at: int

    @staticmethod
    def parse(data):
        return FactionCrimeRewardPayout(
            type=BaseSchema.parse(data.get("type"), FactionOrganizedCrimePayoutType),
            percentage=BaseSchema.parse(data.get("percentage"), int),
            paid_by=BaseSchema.parse(data.get("paid_by"), UserId),
            paid_at=BaseSchema.parse(data.get("paid_at"), int),
        )
