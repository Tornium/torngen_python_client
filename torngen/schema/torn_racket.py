import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_racket_reward import TornRacketReward


@dataclass
class TornRacket(BaseSchema):
    """
    JSON object of `TornRacket`.
    """

    reward: TornRacketReward
    name: str
    level: int
    description: str
    created_at: int
    changed_at: int

    @staticmethod
    def parse(data):
        return TornRacket(
            reward=BaseSchema.parse(data.get("reward"), TornRacketReward),
            name=BaseSchema.parse(data.get("name"), str),
            level=BaseSchema.parse(data.get("level"), int),
            description=BaseSchema.parse(data.get("description"), str),
            created_at=BaseSchema.parse(data.get("created_at"), int),
            changed_at=BaseSchema.parse(data.get("changed_at"), int),
        )
