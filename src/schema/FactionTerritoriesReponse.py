import typing

from FactionTerritory import FactionTerritory

from ..base_schema import BaseSchema


class FactionTerritoriesReponse(BaseSchema):

    territory: typing.List[FactionTerritory]
