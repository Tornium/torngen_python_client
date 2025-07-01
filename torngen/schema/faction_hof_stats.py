import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .hof_value import HofValue
from .hof_value_string import HofValueString


@dataclass
class FactionHofStats(BaseSchema):
    """
    JSON object of `FactionHofStats`.
    """

    respect: HofValue
    rank: HofValueString
    chain: HofValue

    @staticmethod
    def parse(data):
        return FactionHofStats(
            respect=BaseSchema.parse(data.get("respect"), HofValue),
            rank=BaseSchema.parse(data.get("rank"), HofValueString),
            chain=BaseSchema.parse(data.get("chain"), HofValue),
        )
