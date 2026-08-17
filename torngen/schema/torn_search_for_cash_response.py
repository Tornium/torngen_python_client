import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_search_for_cash import TornSearchForCash


@dataclass
class TornSearchForCashResponse(BaseSchema):
    """
    JSON object of `TornSearchForCashResponse`.
    """

    searchforcash: typing.List[TornSearchForCash]

    @staticmethod
    def parse(data):
        return TornSearchForCashResponse(
            searchforcash=BaseSchema.parse(
                data.get("searchforcash"), typing.List[TornSearchForCash]
            ),
        )
