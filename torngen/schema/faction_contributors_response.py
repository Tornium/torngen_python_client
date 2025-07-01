import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_contributor import FactionContributor


@dataclass
class FactionContributorsResponse(BaseSchema):
    """
    JSON object of `FactionContributorsResponse`.
    """

    contributors: typing.List[FactionContributor]

    @staticmethod
    def parse(data):
        return FactionContributorsResponse(
            contributors=BaseSchema.parse(
                data.get("contributors"), typing.List[FactionContributor]
            ),
        )
