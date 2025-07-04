import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_id import UserId


@dataclass
class BazaarWeeklyIncome(BaseSchema):

    weekly_income: int
    name: str
    is_open: bool
    id: UserId

    @staticmethod
    def parse(data):
        return BazaarWeeklyIncome(
            weekly_income=BaseSchema.parse(data.get("weekly_income"), int),
            name=BaseSchema.parse(data.get("name"), str),
            is_open=BaseSchema.parse(data.get("is_open"), bool),
            id=BaseSchema.parse(data.get("id"), UserId),
        )
