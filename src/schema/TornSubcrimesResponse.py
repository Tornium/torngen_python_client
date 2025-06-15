import typing

from TornSubcrime import TornSubcrime

from ..base_schema import BaseSchema


class TornSubcrimesResponse(BaseSchema):

    subcrimes: typing.List[TornSubcrime]
