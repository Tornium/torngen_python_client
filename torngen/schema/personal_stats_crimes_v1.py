import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class PersonalStatsCrimesV1(BaseSchema):
    """
    JSON object of `PersonalStatsCrimesV1`.
    """

    version: str
    total: int
    theft: int
    sell_illegal_goods: int
    other: int
    organized_crimes: int
    murder: int
    fraud: int
    drug_deals: int
    computer: int
    auto_theft: int

    @staticmethod
    def parse(data):
        return PersonalStatsCrimesV1(
            version=BaseSchema.parse(data.get("version"), str),
            total=BaseSchema.parse(data.get("total"), int),
            theft=BaseSchema.parse(data.get("theft"), int),
            sell_illegal_goods=BaseSchema.parse(data.get("sell_illegal_goods"), int),
            other=BaseSchema.parse(data.get("other"), int),
            organized_crimes=BaseSchema.parse(data.get("organized_crimes"), int),
            murder=BaseSchema.parse(data.get("murder"), int),
            fraud=BaseSchema.parse(data.get("fraud"), int),
            drug_deals=BaseSchema.parse(data.get("drug_deals"), int),
            computer=BaseSchema.parse(data.get("computer"), int),
            auto_theft=BaseSchema.parse(data.get("auto_theft"), int),
        )
