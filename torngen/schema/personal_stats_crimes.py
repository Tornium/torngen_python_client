import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .personal_stats_crimes_v1 import PersonalStatsCrimesV1
from .personal_stats_crimes_v2 import PersonalStatsCrimesV2


@dataclass
class PersonalStatsCrimes(BaseSchema):
    """
    JSON object of `PersonalStatsCrimes`.
    """

    crimes: PersonalStatsCrimesV2 | PersonalStatsCrimesV1

    @staticmethod
    def parse(data):
        return PersonalStatsCrimes(
            crimes=BaseSchema.parse(
                data.get("crimes"), PersonalStatsCrimesV2 | PersonalStatsCrimesV1
            ),
        )
