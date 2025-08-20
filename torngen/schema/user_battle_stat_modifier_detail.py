import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class UserBattleStatModifierDetail(BaseSchema):
    """
    JSON object of `UserBattleStatModifierDetail`.
    """

    value: int
    type: str
    effect: str

    @staticmethod
    def parse(data):
        return UserBattleStatModifierDetail(
            value=BaseSchema.parse(data.get("value"), int),
            type=BaseSchema.parse(data.get("type"), str),
            effect=BaseSchema.parse(data.get("effect"), str),
        )
