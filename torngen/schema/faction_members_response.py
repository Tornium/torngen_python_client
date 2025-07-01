import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_member import FactionMember


@dataclass
class FactionMembersResponse(BaseSchema):
    """
    JSON object of `FactionMembersResponse`.
    """

    members: typing.List[FactionMember]

    @staticmethod
    def parse(data):
        return FactionMembersResponse(
            members=BaseSchema.parse(data.get("members"), typing.List[FactionMember]),
        )
