import typing

from FactionTerritoryWarFinished import FactionTerritoryWarFinished
from FactionTerritoryWarOngoing import FactionTerritoryWarOngoing

from ..base_schema import BaseSchema


class FactionTerritoryWarsResponse(BaseSchema):

    territorywars: (
        typing.List[FactionTerritoryWarFinished]
        | typing.List[FactionTerritoryWarOngoing]
    )
