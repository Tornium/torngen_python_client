import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .bazaar_specialized import BazaarSpecialized
from .bazaar_weekly import BazaarWeekly


@dataclass
class BazaarResponse(BaseSchema):
    """
    JSON object of `BazaarResponse`.
    """

    bazaar: BazaarSpecialized | BazaarWeekly

    @staticmethod
    def parse(data):
        return BazaarResponse(
            bazaar=BaseSchema.parse(
                data.get("bazaar"), BazaarSpecialized | BazaarWeekly
            ),
        )
