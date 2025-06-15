import typing

from TornRacket import TornRacket

from ..base_schema import BaseSchema


class FactionRacketsReponse(BaseSchema):

    rackets: typing.List[TornRacket]
