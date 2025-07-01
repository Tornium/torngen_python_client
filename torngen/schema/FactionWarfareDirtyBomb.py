import typing

from DirtyBombId import DirtyBombId
from FactionWarfareDirtyBombPlanter import FactionWarfareDirtyBombPlanter
from FactionWarfareDirtyBombTargetFaction import \
    FactionWarfareDirtyBombTargetFaction

from ..base_schema import BaseSchema


class FactionWarfareDirtyBomb(BaseSchema):

    user: None | FactionWarfareDirtyBombPlanter
    planted_at: int
    id: DirtyBombId
    faction: FactionWarfareDirtyBombTargetFaction
    detonated_at: int
