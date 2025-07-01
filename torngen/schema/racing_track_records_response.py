import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .race_record import RaceRecord


@dataclass
class RacingTrackRecordsResponse(BaseSchema):
    """
    JSON object of `RacingTrackRecordsResponse`.
    """

    records: typing.List[RaceRecord]

    @staticmethod
    def parse(data):
        return RacingTrackRecordsResponse(
            records=BaseSchema.parse(data.get("records"), typing.List[RaceRecord]),
        )
