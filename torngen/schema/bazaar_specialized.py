import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .bazaar_weekly_customers import BazaarWeeklyCustomers


@dataclass
class BazaarSpecialized(BaseSchema):
    """
    JSON object of `BazaarSpecialized`.
    """

    specialized: typing.List[BazaarWeeklyCustomers]

    @staticmethod
    def parse(data):
        return BazaarSpecialized(
            specialized=BaseSchema.parse(
                data.get("specialized"), typing.List[BazaarWeeklyCustomers]
            ),
        )
