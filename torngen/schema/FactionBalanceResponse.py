import typing

from FactionBalance import FactionBalance

from ..base_schema import BaseSchema


class FactionBalanceResponse(BaseSchema):

    balance: FactionBalance
