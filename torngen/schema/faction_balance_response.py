import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_balance import FactionBalance


@dataclass
class FactionBalanceResponse(BaseSchema):
    """
    JSON object of `FactionBalanceResponse`.
    """

    balance: FactionBalance

    @staticmethod
    def parse(data):
        return FactionBalanceResponse(
            balance=BaseSchema.parse(data.get("balance"), FactionBalance),
        )
