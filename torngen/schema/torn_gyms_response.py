import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .torn_gym import TornGym


@dataclass
class TornGymsResponse(BaseSchema):
    """
    JSON object of `TornGymsResponse`.
    """

    gyms: typing.List[TornGym]

    @staticmethod
    def parse(data):
        return TornGymsResponse(
            gyms=BaseSchema.parse(data.get("gyms"), typing.List[TornGym]),
        )
