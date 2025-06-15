import typing

from FactionId import FactionId

from ..base_schema import BaseSchema


class FactionPact(BaseSchema):

    until: str
    faction_name: str
    faction_id: FactionId
