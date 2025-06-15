import typing

from RaceRecord import RaceRecord

from ..base_schema import BaseSchema


class RacingTrackRecordsResponse(BaseSchema):

    records: typing.List[RaceRecord]
