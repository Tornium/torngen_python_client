import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_id import UserId


@dataclass
class ReportWarrantDetails(BaseSchema):
    """
    JSON object of `ReportWarrantDetails`.
    """

    warrant: int
    name: str
    id: UserId

    @staticmethod
    def parse(data):
        return ReportWarrantDetails(
            warrant=BaseSchema.parse(data.get("warrant"), int),
            name=BaseSchema.parse(data.get("name"), str),
            id=BaseSchema.parse(data.get("id"), UserId),
        )
