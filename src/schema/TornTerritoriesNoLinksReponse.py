import typing

from TornTerritory import TornTerritory

from ..base_schema import BaseSchema


class TornTerritoriesNoLinksReponse(BaseSchema):

    territory: typing.List[TornTerritory]
