import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_id import FactionId
from .report_type_enum import ReportTypeEnum
from .user_id import UserId


@dataclass
class ReportBase(BaseSchema):
    """
    JSON object of `ReportBase`.
    """

    type: ReportTypeEnum
    timestamp: int
    target_id: None | UserId
    reporter_id: UserId
    faction_id: None | FactionId

    @staticmethod
    def parse(data):
        return ReportBase(
            type=BaseSchema.parse(data.get("type"), ReportTypeEnum),
            timestamp=BaseSchema.parse(data.get("timestamp"), int),
            target_id=BaseSchema.parse(data.get("target_id"), None | UserId),
            reporter_id=BaseSchema.parse(data.get("reporter_id"), UserId),
            faction_id=BaseSchema.parse(data.get("faction_id"), None | FactionId),
        )
