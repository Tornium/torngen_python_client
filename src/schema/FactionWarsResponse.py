import typing

from FactionPact import FactionPact
from FactionWars import FactionWars

from ..base_schema import BaseSchema


class FactionWarsResponse(BaseSchema):

    wars: FactionWars
    pacts: typing.List[FactionPact]
