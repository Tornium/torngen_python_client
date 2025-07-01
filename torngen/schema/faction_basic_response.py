import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .faction_basic import FactionBasic


@dataclass
class FactionBasicResponse(BaseSchema):
    """
    JSON object of `FactionBasicResponse`.
    """

    basic: FactionBasic

    @staticmethod
    def parse(data):
        return FactionBasicResponse(
            basic=BaseSchema.parse(data.get("basic"), FactionBasic),
        )
