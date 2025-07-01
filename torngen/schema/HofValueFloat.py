import typing

from ..base_schema import BaseSchema


class HofValueFloat(BaseSchema):

    value: int | float
    rank: int
