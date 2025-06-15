import typing

from TornItemArmorCoveragePartEnum import TornItemArmorCoveragePartEnum

from ..base_schema import BaseSchema


class TornItemArmorCoverage(BaseSchema):

    value: int | float
    name: TornItemArmorCoveragePartEnum
