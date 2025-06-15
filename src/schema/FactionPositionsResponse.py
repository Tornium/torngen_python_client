import typing

from FactionPosition import FactionPosition

from ..base_schema import BaseSchema


class FactionPositionsResponse(BaseSchema):

    positions: typing.List[FactionPosition]
