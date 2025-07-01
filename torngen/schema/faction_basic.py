import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_id import FactionId
from .faction_rank import FactionRank
from .user_id import UserId


@dataclass
class FactionBasic(BaseSchema):
    """
    JSON object of `FactionBasic`.
    """

    tag_image: str
    tag: str
    respect: int
    rank: FactionRank
    name: str
    members: int
    leader_id: UserId
    is_enlisted: None | bool
    id: FactionId
    days_old: int
    co_leader_id: UserId
    capacity: int
    best_chain: int

    @staticmethod
    def parse(data):
        return FactionBasic(
            tag_image=BaseSchema.parse(data.get("tag_image"), str),
            tag=BaseSchema.parse(data.get("tag"), str),
            respect=BaseSchema.parse(data.get("respect"), int),
            rank=BaseSchema.parse(data.get("rank"), FactionRank),
            name=BaseSchema.parse(data.get("name"), str),
            members=BaseSchema.parse(data.get("members"), int),
            leader_id=BaseSchema.parse(data.get("leader_id"), UserId),
            is_enlisted=BaseSchema.parse(data.get("is_enlisted"), None | bool),
            id=BaseSchema.parse(data.get("id"), FactionId),
            days_old=BaseSchema.parse(data.get("days_old"), int),
            co_leader_id=BaseSchema.parse(data.get("co_leader_id"), UserId),
            capacity=BaseSchema.parse(data.get("capacity"), int),
            best_chain=BaseSchema.parse(data.get("best_chain"), int),
        )
