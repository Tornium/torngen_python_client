import typing

from FactionStatEnum import FactionStatEnum

from ..base_schema import BaseSchema


class FactionStat(BaseSchema):

    value: int
    name: FactionStatEnum
