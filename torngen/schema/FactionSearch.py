import typing

from FactionId import FactionId
from FactionSearchLeader import FactionSearchLeader

from ..base_schema import BaseSchema


class FactionSearch(BaseSchema):

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
