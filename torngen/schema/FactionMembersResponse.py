import typing

from FactionMember import FactionMember

from ..base_schema import BaseSchema


class FactionMembersResponse(BaseSchema):

    members: typing.List[FactionMember]
