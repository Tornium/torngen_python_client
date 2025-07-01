import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .log_id import LogId


@dataclass
class TornLog(BaseSchema):
    """
    JSON object of `TornLog`.
    """

    title: str
    id: LogId

    @staticmethod
    def parse(data):
        return TornLog(
            title=BaseSchema.parse(data.get("title"), str),
            id=BaseSchema.parse(data.get("id"), LogId),
        )
