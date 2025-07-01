import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_application import FactionApplication


@dataclass
class FactionApplicationsResponse(BaseSchema):
    """
    JSON object of `FactionApplicationsResponse`.
    """

    applications: typing.List[FactionApplication]

    @staticmethod
    def parse(data):
        return FactionApplicationsResponse(
            applications=BaseSchema.parse(
                data.get("applications"), typing.List[FactionApplication]
            ),
        )
