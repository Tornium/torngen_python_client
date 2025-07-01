import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_log import TornLog


@dataclass
class TornLogTypesResponse(BaseSchema):
    """
    JSON object of `TornLogTypesResponse`.
    """

    logtypes: typing.List[TornLog]

    @staticmethod
    def parse(data):
        return TornLogTypesResponse(
            logtypes=BaseSchema.parse(data.get("logtypes"), typing.List[TornLog]),
        )
