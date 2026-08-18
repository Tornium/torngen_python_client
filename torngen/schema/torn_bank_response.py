import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_bank import TornBank


@dataclass
class TornBankResponse(BaseSchema):
    """
    JSON object of `TornBankResponse`.
    """

    bank: typing.List[TornBank]

    @staticmethod
    def parse(data):
        return TornBankResponse(
            bank=BaseSchema.parse(data.get("bank"), typing.List[TornBank]),
        )
