import typing

from FactionOrganizedCrimePayoutType import FactionOrganizedCrimePayoutType
from UserId import UserId

from ..base_schema import BaseSchema


class FactionCrimeRewardPayout(BaseSchema):

    type: FactionOrganizedCrimePayoutType
    percentage: int
    paid_by: UserId
    paid_at: int
