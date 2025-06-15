import typing

from MarketSelectionName import MarketSelectionName

from ..base_schema import BaseSchema


class MarketLookupResponse(BaseSchema):

    selections: typing.List[MarketSelectionName]
