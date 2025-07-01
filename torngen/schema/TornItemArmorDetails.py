import typing

from TornItemArmorCoverage import TornItemArmorCoverage
from TornItemBaseStats import TornItemBaseStats

from ..base_schema import BaseSchema


class TornItemArmorDetails(BaseSchema):

    coverage: typing.List[TornItemArmorCoverage]
    base_stats: TornItemBaseStats
