import typing

from TornFactionTree import TornFactionTree

from ..base_schema import BaseSchema


class TornFactionTreeResponse(BaseSchema):

    factionTree: typing.List[TornFactionTree]
