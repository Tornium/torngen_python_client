import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .bazaar_specialized import BazaarSpecialized


@dataclass
class BazaarResponseSpecialized(BaseSchema):
    """
    JSON object of `BazaarResponseSpecialized`.
    """

    bazaar: BazaarSpecialized

    @staticmethod
    def parse(data):
        return BazaarResponseSpecialized(
            bazaar=BaseSchema.parse(data.get("bazaar"), BazaarSpecialized),
        )
