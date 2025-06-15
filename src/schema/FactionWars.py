import typing

from FactionRaidWar import FactionRaidWar
from FactionRankedWar import FactionRankedWar
from FactionTerritoryWar import FactionTerritoryWar

from ..base_schema import BaseSchema


class FactionWars(BaseSchema):

    territory: typing.List[FactionTerritoryWar]
    ranked: None | FactionRankedWar
    raids: typing.List[FactionRaidWar]
