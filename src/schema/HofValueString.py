import typing

from ..base_schema import BaseSchema


class HofValueString(BaseSchema):

    value: str
    rank: None | int
