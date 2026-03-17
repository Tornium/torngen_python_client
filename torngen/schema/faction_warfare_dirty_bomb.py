import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .dirty_bomb_id import DirtyBombId
from .faction_warfare_dirty_bomb_planter import FactionWarfareDirtyBombPlanter
from .faction_warfare_dirty_bomb_target_faction import \
    FactionWarfareDirtyBombTargetFaction


@dataclass
class FactionWarfareDirtyBomb(BaseSchema):
    """
    JSON object of `FactionWarfareDirtyBomb`.
    """

    user: None | FactionWarfareDirtyBombPlanter
    planted_at: int
    id: DirtyBombId
    faction: FactionWarfareDirtyBombTargetFaction
    detonated_at: int

    @staticmethod
    def parse(data):
        return FactionWarfareDirtyBomb(
            user=BaseSchema.parse(
                data.get("user"), None | FactionWarfareDirtyBombPlanter
            ),
            planted_at=BaseSchema.parse(data.get("planted_at"), int),
            id=BaseSchema.parse(data.get("id"), DirtyBombId),
            faction=BaseSchema.parse(
                data.get("faction"), FactionWarfareDirtyBombTargetFaction
            ),
            detonated_at=BaseSchema.parse(data.get("detonated_at"), int),
        )
