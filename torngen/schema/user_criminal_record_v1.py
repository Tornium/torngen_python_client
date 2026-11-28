import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class UserCriminalRecordV1(BaseSchema):
    """
    JSON object of `UserCriminalRecordV1`.
    """

    version: typing.Literal["v1"]
    total: int
    theft: int
    sell_illegal_goods: int
    other: int
    murder: int
    fraud: int
    drug_deals: int
    computer: int
    auto_theft: int

    @staticmethod
    def parse(data):
        return UserCriminalRecordV1(
            version=BaseSchema.parse(data.get("version"), typing.Literal["v1"]),
            total=BaseSchema.parse(data.get("total"), int),
            theft=BaseSchema.parse(data.get("theft"), int),
            sell_illegal_goods=BaseSchema.parse(data.get("sell_illegal_goods"), int),
            other=BaseSchema.parse(data.get("other"), int),
            murder=BaseSchema.parse(data.get("murder"), int),
            fraud=BaseSchema.parse(data.get("fraud"), int),
            drug_deals=BaseSchema.parse(data.get("drug_deals"), int),
            computer=BaseSchema.parse(data.get("computer"), int),
            auto_theft=BaseSchema.parse(data.get("auto_theft"), int),
        )
