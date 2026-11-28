import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class FactionOcHistorySpawnDetails(BaseSchema):
    """
    JSON object of `FactionOcHistorySpawnDetails`.
    """

    scope: int

    @staticmethod
    def parse(data):
        return FactionOcHistorySpawnDetails(
            scope=BaseSchema.parse(data.get("scope"), int),
        )
