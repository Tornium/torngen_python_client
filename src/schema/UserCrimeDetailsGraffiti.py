import typing

from ..base_schema import BaseSchema


class UserCrimeDetailsGraffiti(BaseSchema):

    most_graffiti_simultaneously: int
    most_graffiti_in_one_area: int
    graffiti_removed: int
    cost_to_city: int
    cans_used: int
