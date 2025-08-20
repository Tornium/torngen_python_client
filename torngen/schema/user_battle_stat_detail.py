import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_battle_stat_modifier_detail import UserBattleStatModifierDetail


@dataclass
class UserBattleStatDetail(BaseSchema):
    """
    JSON object of `UserBattleStatDetail`.
    """

    value: int
    modifiers: typing.List[UserBattleStatModifierDetail]
    modifier: int

    @staticmethod
    def parse(data):
        return UserBattleStatDetail(
            value=BaseSchema.parse(data.get("value"), int),
            modifiers=BaseSchema.parse(
                data.get("modifiers"), typing.List[UserBattleStatModifierDetail]
            ),
            modifier=BaseSchema.parse(data.get("modifier"), int),
        )
