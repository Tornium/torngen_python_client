import typing

from ..base_schema import BaseSchema


class PersonalStatsCrimesV1(BaseSchema):

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
