import typing

from ..base_schema import BaseSchema


class UserFactionBalance(BaseSchema):

    points: int
    money: int
