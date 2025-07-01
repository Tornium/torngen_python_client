import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class UserCrimeDetailsGraffiti(BaseSchema):
    """
    JSON object of `UserCrimeDetailsGraffiti`.
    """

    most_graffiti_simultaneously: int
    most_graffiti_in_one_area: int
    graffiti_removed: int
    cost_to_city: int
    cans_used: int

    @staticmethod
    def parse(data):
        return UserCrimeDetailsGraffiti(
            most_graffiti_simultaneously=BaseSchema.parse(
                data.get("most_graffiti_simultaneously"), int
            ),
            most_graffiti_in_one_area=BaseSchema.parse(
                data.get("most_graffiti_in_one_area"), int
            ),
            graffiti_removed=BaseSchema.parse(data.get("graffiti_removed"), int),
            cost_to_city=BaseSchema.parse(data.get("cost_to_city"), int),
            cans_used=BaseSchema.parse(data.get("cans_used"), int),
        )
