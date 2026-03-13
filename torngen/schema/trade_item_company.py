import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .company_id import CompanyId
from .user_id import UserId


@dataclass
class TradeItemCompany(BaseSchema):
    """
    JSON object of `TradeItemCompany`.
    """

    user_id: UserId
    type: typing.Literal["Company"]
    details: typing.TypedDict("", {"value": int, "name": str, "id": CompanyId})

    @staticmethod
    def parse(data):
        return TradeItemCompany(
            user_id=BaseSchema.parse(data.get("user_id"), UserId),
            type=BaseSchema.parse(data.get("type"), typing.Literal["Company"]),
            details=BaseSchema.parse(
                data.get("details"),
                typing.TypedDict("", {"value": int, "name": str, "id": CompanyId}),
            ),
        )
