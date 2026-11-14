import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_headline import TornHeadline


@dataclass
class TornHeadlinesResponse(BaseSchema):
    """
    JSON object of `TornHeadlinesResponse`.
    """

    headlines: typing.List[TornHeadline]

    @staticmethod
    def parse(data):
        return TornHeadlinesResponse(
            headlines=BaseSchema.parse(
                data.get("headlines"), typing.List[TornHeadline]
            ),
        )
