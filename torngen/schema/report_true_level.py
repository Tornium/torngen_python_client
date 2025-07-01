import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ReportTrueLevel(BaseSchema):
    """
    JSON object of `ReportTrueLevel`.
    """

    level: int

    @staticmethod
    def parse(data):
        return ReportTrueLevel(
            level=BaseSchema.parse(data.get("level"), int),
        )
