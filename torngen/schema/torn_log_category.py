import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .log_category_id import LogCategoryId


@dataclass
class TornLogCategory(BaseSchema):
    """
    JSON object of `TornLogCategory`.
    """

    title: str
    id: LogCategoryId

    @staticmethod
    def parse(data):
        return TornLogCategory(
            title=BaseSchema.parse(data.get("title"), str),
            id=BaseSchema.parse(data.get("id"), LogCategoryId),
        )
