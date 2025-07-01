import typing

from FactionId import FactionId
from FactionRank import FactionRank
from UserId import UserId

from ..base_schema import BaseSchema


class FactionBasic(BaseSchema):

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
