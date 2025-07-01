import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_id import FactionId
from .faction_search_leader import FactionSearchLeader


@dataclass
class FactionSearch(BaseSchema):
    """
    JSON object of `FactionSearch`.
    """

    tag_image: None | str
    tag: None | str
    respect: int
    name: str
    members: int
    leader: FactionSearchLeader
    is_recruiting: bool
    is_destroyed: bool
    image: None | str
    id: FactionId
    co_leader: None | FactionSearchLeader

    @staticmethod
    def parse(data):
        return FactionSearch(
            tag_image=BaseSchema.parse(data.get("tag_image"), None | str),
            tag=BaseSchema.parse(data.get("tag"), None | str),
            respect=BaseSchema.parse(data.get("respect"), int),
            name=BaseSchema.parse(data.get("name"), str),
            members=BaseSchema.parse(data.get("members"), int),
            leader=BaseSchema.parse(data.get("leader"), FactionSearchLeader),
            is_recruiting=BaseSchema.parse(data.get("is_recruiting"), bool),
            is_destroyed=BaseSchema.parse(data.get("is_destroyed"), bool),
            image=BaseSchema.parse(data.get("image"), None | str),
            id=BaseSchema.parse(data.get("id"), FactionId),
            co_leader=BaseSchema.parse(
                data.get("co_leader"), None | FactionSearchLeader
            ),
        )
