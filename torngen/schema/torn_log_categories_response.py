import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_log_category import TornLogCategory


@dataclass
class TornLogCategoriesResponse(BaseSchema):
    """
    JSON object of `TornLogCategoriesResponse`.
    """

    logcategories: typing.List[TornLogCategory]

    @staticmethod
    def parse(data):
        return TornLogCategoriesResponse(
            logcategories=BaseSchema.parse(
                data.get("logcategories"), typing.List[TornLogCategory]
            ),
        )
