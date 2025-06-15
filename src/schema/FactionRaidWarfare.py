import typing

from FactionRaidWarfareFaction import FactionRaidWarfareFaction
from RaidWarId import RaidWarId

from ..base_schema import BaseSchema


class FactionRaidWarfare(BaseSchema):

    start: int
    id: RaidWarId
    end: None | int
    defender: FactionRaidWarfareFaction
    aggressor: FactionRaidWarfareFaction
