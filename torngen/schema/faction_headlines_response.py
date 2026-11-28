import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_headline import TornHeadline


@dataclass
class FactionHeadlinesResponse(BaseSchema):
    """
    JSON object of `FactionHeadlinesResponse`.
    """

    headlines: typing.List[TornHeadline]

    @staticmethod
    def parse(data):
        return FactionHeadlinesResponse(
            headlines=BaseSchema.parse(
                data.get("headlines"), typing.List[TornHeadline]
            ),
        )
