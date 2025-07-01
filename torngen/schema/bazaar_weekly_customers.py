import typing

from ..base_schema import BaseSchema
from .bazaar import Bazaar


class BazaarWeeklyCustomers(BaseSchema):
    value: typing.List[typing.TypedDict("", {"weekly_customers": int}) | Bazaar]
