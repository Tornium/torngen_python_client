import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_crime_id import FactionCrimeId
from .faction_crime_reward import FactionCrimeReward
from .faction_crime_slot import FactionCrimeSlot
from .faction_crime_status_enum import FactionCrimeStatusEnum
from .organized_crime_name import OrganizedCrimeName


@dataclass
class FactionCrime(BaseSchema):
    """
    JSON object of `FactionCrime`.
    """

    status: FactionCrimeStatusEnum
    slots: typing.List[FactionCrimeSlot]
    rewards: None | FactionCrimeReward
    ready_at: None | int
    previous_crime_id: None | FactionCrimeId
    planning_at: None | int
    name: OrganizedCrimeName
    id: FactionCrimeId
    expired_at: int
    executed_at: None | int
    difficulty: int
    created_at: int

    @staticmethod
    def parse(data):
        return FactionCrime(
            status=BaseSchema.parse(data.get("status"), FactionCrimeStatusEnum),
            slots=BaseSchema.parse(data.get("slots"), typing.List[FactionCrimeSlot]),
            rewards=BaseSchema.parse(data.get("rewards"), None | FactionCrimeReward),
            ready_at=BaseSchema.parse(data.get("ready_at"), None | int),
            previous_crime_id=BaseSchema.parse(
                data.get("previous_crime_id"), None | FactionCrimeId
            ),
            planning_at=BaseSchema.parse(data.get("planning_at"), None | int),
            name=BaseSchema.parse(data.get("name"), OrganizedCrimeName),
            id=BaseSchema.parse(data.get("id"), FactionCrimeId),
            expired_at=BaseSchema.parse(data.get("expired_at"), int),
            executed_at=BaseSchema.parse(data.get("executed_at"), None | int),
            difficulty=BaseSchema.parse(data.get("difficulty"), int),
            created_at=BaseSchema.parse(data.get("created_at"), int),
        )
