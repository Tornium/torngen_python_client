import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema


@dataclass
class PersonalStatsBattleStats(BaseSchema):
    """
    JSON object of `PersonalStatsBattleStats`.
    """

    battle_stats: typing.TypedDict(
        "",
        {"total": int, "strength": int, "speed": int, "dexterity": int, "defense": int},
    )

    @staticmethod
    def parse(data):
        return PersonalStatsBattleStats(
            battle_stats=BaseSchema.parse(
                data.get("battle_stats"),
                typing.TypedDict(
                    "",
                    {
                        "total": int,
                        "strength": int,
                        "speed": int,
                        "dexterity": int,
                        "defense": int,
                    },
                ),
            ),
        )
