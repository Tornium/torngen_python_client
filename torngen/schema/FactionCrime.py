import typing

from FactionCrimeId import FactionCrimeId
from FactionCrimeReward import FactionCrimeReward
from FactionCrimeSlot import FactionCrimeSlot
from FactionCrimeStatusEnum import FactionCrimeStatusEnum

from ..base_schema import BaseSchema


class FactionCrime(BaseSchema):

    status: FactionCrimeStatusEnum
    slots: typing.List[FactionCrimeSlot]
    rewards: None | FactionCrimeReward
    ready_at: None | int
    previous_crime_id: None | FactionCrimeId
    planning_at: None | int
    name: str
    id: FactionCrimeId
    expired_at: int
    executed_at: None | int
    difficulty: int
    created_at: int
