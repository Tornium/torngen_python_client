import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_id import FactionId
from .user_id import UserId
from .user_rank_enum import UserRankEnum


@dataclass
class TornHofBasic(BaseSchema):
    """
    JSON object of `TornHofBasic`.
    """

    value: int | float | str | int
    username: str
    signed_up: int
    rank_number: int
    rank_name: UserRankEnum
    rank: str
    position: int
    level: int
    last_action: int
    id: UserId
    faction_id: FactionId
    age_in_days: int

    @staticmethod
    def parse(data):
        return TornHofBasic(
            value=BaseSchema.parse(data.get("value"), int | float | str | int),
            username=BaseSchema.parse(data.get("username"), str),
            signed_up=BaseSchema.parse(data.get("signed_up"), int),
            rank_number=BaseSchema.parse(data.get("rank_number"), int),
            rank_name=BaseSchema.parse(data.get("rank_name"), UserRankEnum),
            rank=BaseSchema.parse(data.get("rank"), str),
            position=BaseSchema.parse(data.get("position"), int),
            level=BaseSchema.parse(data.get("level"), int),
            last_action=BaseSchema.parse(data.get("last_action"), int),
            id=BaseSchema.parse(data.get("id"), UserId),
            faction_id=BaseSchema.parse(data.get("faction_id"), FactionId),
            age_in_days=BaseSchema.parse(data.get("age_in_days"), int),
        )
