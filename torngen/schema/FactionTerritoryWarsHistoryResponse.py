import typing

from FactionTerritoryWarFinished import FactionTerritoryWarFinished

from ..base_schema import BaseSchema


class FactionTerritoryWarsHistoryResponse(BaseSchema):

    territorywars: typing.List[FactionTerritoryWarFinished]
