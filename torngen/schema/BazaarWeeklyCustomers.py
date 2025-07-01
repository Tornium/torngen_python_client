import typing

from Bazaar import Bazaar

from ..base_schema import BaseSchema


class BazaarWeeklyCustomers(BaseSchema):
    value: typing.List[typing.TypedDict("", {"weekly_customers": int}) | Bazaar]
