import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .hof_value import HofValue
from .hof_value_float import HofValueFloat


@dataclass
class UserHofStats(BaseSchema):
    """
    JSON object of `UserHofStats`.
    """

    working_stats: HofValue
    travel_time: HofValue
    revives: HofValue
    rank: HofValue
    racing_wins: HofValue
    racing_skill: HofValueFloat
    racing_points: HofValue
    offences: HofValue
    networth: HofValue
    level: HofValue
    defends: HofValue
    busts: HofValue
    battle_stats: None | HofValue
    awards: HofValue
    attacks: HofValue

    @staticmethod
    def parse(data):
        return UserHofStats(
            working_stats=BaseSchema.parse(data.get("working_stats"), HofValue),
            travel_time=BaseSchema.parse(data.get("travel_time"), HofValue),
            revives=BaseSchema.parse(data.get("revives"), HofValue),
            rank=BaseSchema.parse(data.get("rank"), HofValue),
            racing_wins=BaseSchema.parse(data.get("racing_wins"), HofValue),
            racing_skill=BaseSchema.parse(data.get("racing_skill"), HofValueFloat),
            racing_points=BaseSchema.parse(data.get("racing_points"), HofValue),
            offences=BaseSchema.parse(data.get("offences"), HofValue),
            networth=BaseSchema.parse(data.get("networth"), HofValue),
            level=BaseSchema.parse(data.get("level"), HofValue),
            defends=BaseSchema.parse(data.get("defends"), HofValue),
            busts=BaseSchema.parse(data.get("busts"), HofValue),
            battle_stats=BaseSchema.parse(data.get("battle_stats"), None | HofValue),
            awards=BaseSchema.parse(data.get("awards"), HofValue),
            attacks=BaseSchema.parse(data.get("attacks"), HofValue),
        )
