import typing

from ..base_schema import BaseSchema
from .bazaar import Bazaar


class BazaarWeeklyIncome(BaseSchema):
    value: typing.List[typing.TypedDict("", {"weekly_income": int}) | Bazaar]
