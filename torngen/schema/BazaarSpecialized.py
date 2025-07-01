import typing

from BazaarWeeklyCustomers import BazaarWeeklyCustomers

from ..base_schema import BaseSchema


class BazaarSpecialized(BaseSchema):

    specialized: typing.List[BazaarWeeklyCustomers]
