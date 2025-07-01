import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class ReportStats(BaseSchema):
    """
    JSON object of `ReportStats`.
    """

    total: None | int
    strength: None | int
    speed: None | int
    dexterity: None | int
    defense: None | int

    @staticmethod
    def parse(data):
        return ReportStats(
            total=BaseSchema.parse(data.get("total"), None | int),
            strength=BaseSchema.parse(data.get("strength"), None | int),
            speed=BaseSchema.parse(data.get("speed"), None | int),
            dexterity=BaseSchema.parse(data.get("dexterity"), None | int),
            defense=BaseSchema.parse(data.get("defense"), None | int),
        )
