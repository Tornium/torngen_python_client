import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_id import UserId


@dataclass
class BazaarWeeklyCustomers(BaseSchema):

    weekly_customers: int
    name: str
    is_open: bool
    id: UserId

    @staticmethod
    def parse(data):
        return BazaarWeeklyCustomers(
            weekly_customers=BaseSchema.parse(data.get("weekly_customers"), int),
            name=BaseSchema.parse(data.get("name"), str),
            is_open=BaseSchema.parse(data.get("is_open"), bool),
            id=BaseSchema.parse(data.get("id"), UserId),
        )
