import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class FactionHofValues(BaseSchema):
    """
    JSON object of `FactionHofValues`.
    """

    respect: None | int
    chain_duration: None | int
    chain: None | int

    @staticmethod
    def parse(data):
        return FactionHofValues(
            respect=BaseSchema.parse(data.get("respect"), None | int),
            chain_duration=BaseSchema.parse(data.get("chain_duration"), None | int),
            chain=BaseSchema.parse(data.get("chain"), None | int),
        )
