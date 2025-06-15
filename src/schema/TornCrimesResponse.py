import typing

from TornCrime import TornCrime

from ..base_schema import BaseSchema


class TornCrimesResponse(BaseSchema):

    crimes: typing.List[TornCrime]
