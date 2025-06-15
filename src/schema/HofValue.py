import typing

from ..base_schema import BaseSchema


class HofValue(BaseSchema):

    value: int
    rank: int
