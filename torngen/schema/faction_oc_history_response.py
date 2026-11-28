import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_oc_history import FactionOcHistory


@dataclass
class FactionOcHistoryResponse(BaseSchema):
    """
    JSON object of `FactionOcHistoryResponse`.
    """

    ochistory: FactionOcHistory

    @staticmethod
    def parse(data):
        return FactionOcHistoryResponse(
            ochistory=BaseSchema.parse(data.get("ochistory"), FactionOcHistory),
        )
