import typing

from Bazaar import Bazaar

from ..base_schema import BaseSchema


class BazaarWeeklyIncome(BaseSchema):
    value: typing.List[typing.TypedDict("", {"weekly_income": int}) | Bazaar]
