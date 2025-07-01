import typing

from ..base_schema import BaseSchema


class PersonalStatsBattleStats(BaseSchema):

    battle_stats: typing.TypedDict(
        "",
        {"total": int, "strength": int, "speed": int, "dexterity": int, "defense": int},
    )
