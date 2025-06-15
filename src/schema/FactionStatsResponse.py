import typing

from FactionStat import FactionStat

from ..base_schema import BaseSchema


class FactionStatsResponse(BaseSchema):

    stats: typing.List[FactionStat]
