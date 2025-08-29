import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_honor import TornHonor


@dataclass
class TornHonorsResponse(BaseSchema):
    """
    JSON object of `TornHonorsResponse`.
    """

    honors: typing.List[TornHonor]

    @staticmethod
    def parse(data):
        return TornHonorsResponse(
            honors=BaseSchema.parse(data.get("honors"), typing.List[TornHonor]),
        )
