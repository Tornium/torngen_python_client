import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_raid_warfare_faction import FactionRaidWarfareFaction
from .raid_war_id import RaidWarId


@dataclass
class FactionRaidWarfare(BaseSchema):
    """
    JSON object of `FactionRaidWarfare`.
    """

    start: int
    id: RaidWarId
    end: None | int
    defender: FactionRaidWarfareFaction
    aggressor: FactionRaidWarfareFaction

    @staticmethod
    def parse(data):
        return FactionRaidWarfare(
            start=BaseSchema.parse(data.get("start"), int),
            id=BaseSchema.parse(data.get("id"), RaidWarId),
            end=BaseSchema.parse(data.get("end"), None | int),
            defender=BaseSchema.parse(data.get("defender"), FactionRaidWarfareFaction),
            aggressor=BaseSchema.parse(
                data.get("aggressor"), FactionRaidWarfareFaction
            ),
        )
