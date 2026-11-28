import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class FactionOcHistoryPunishmentDetails(BaseSchema):
    """
    JSON object of `FactionOcHistoryPunishmentDetails`.
    """

    reason: None | str
    duration: int

    @staticmethod
    def parse(data):
        return FactionOcHistoryPunishmentDetails(
            reason=BaseSchema.parse(data.get("reason"), None | str),
            duration=BaseSchema.parse(data.get("duration"), int),
        )
