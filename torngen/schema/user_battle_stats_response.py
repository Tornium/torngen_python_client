import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .user_battle_stat_detail import UserBattleStatDetail


@dataclass
class UserBattleStatsResponse(BaseSchema):
    """
    JSON object of `UserBattleStatsResponse`.
    """

    battlestats: typing.TypedDict(
        "",
        {
            "total": int,
            "strength": UserBattleStatDetail,
            "speed": UserBattleStatDetail,
            "dexterity": UserBattleStatDetail,
            "defense": UserBattleStatDetail,
        },
    )

    @staticmethod
    def parse(data):
        return UserBattleStatsResponse(
            battlestats=BaseSchema.parse(
                data.get("battlestats"),
                typing.TypedDict(
                    "",
                    {
                        "total": int,
                        "strength": UserBattleStatDetail,
                        "speed": UserBattleStatDetail,
                        "dexterity": UserBattleStatDetail,
                        "defense": UserBattleStatDetail,
                    },
                ),
            ),
        )
