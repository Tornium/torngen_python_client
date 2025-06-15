import typing

from TornRacketReward import TornRacketReward

from ..base_schema import BaseSchema


class TornRacket(BaseSchema):

    reward: TornRacketReward
    name: str
    level: int
    description: str
    created_at: int
    changed_at: int
