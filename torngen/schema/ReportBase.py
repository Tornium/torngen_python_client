import typing

from FactionId import FactionId
from ReportTypeEnum import ReportTypeEnum
from UserId import UserId

from ..base_schema import BaseSchema


class ReportBase(BaseSchema):

    type: ReportTypeEnum
    timestamp: int
    target_id: None | UserId
    reporter_id: UserId
    faction_id: None | FactionId
