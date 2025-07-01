import typing

from HofValue import HofValue
from HofValueFloat import HofValueFloat

from ..base_schema import BaseSchema


class UserHofStats(BaseSchema):

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
