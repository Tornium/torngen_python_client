import typing

from FactionHofStats import FactionHofStats

from ..base_schema import BaseSchema


class FactionHofResponse(BaseSchema):

    hof: FactionHofStats
