import typing

from AttackCode import AttackCode
from AttackId import AttackId
from AttackingFinishingHitEffects import AttackingFinishingHitEffects
from AttackPlayer import AttackPlayer
from FactionAttackResult import FactionAttackResult

from ..base_schema import BaseSchema


class Attack(BaseSchema):

    started: int
    result: FactionAttackResult
    respect_loss: int | float
    respect_gain: int | float
    modifiers: typing.TypedDict(
        "",
        {
            "warlord": int | float,
            "war": int | float,
            "retaliation": int | float,
            "overseas": int | float,
            "group": int | float,
            "fair_fight": int | float,
            "chain": int | float,
        },
    )
    is_stealthed: bool
    is_ranked_war: bool
    is_raid: bool
    is_interrupted: bool
    id: AttackId
    finishing_hit_effects: typing.List[AttackingFinishingHitEffects]
    ended: int
    defender: AttackPlayer
    code: AttackCode
    chain: int
    attacker: None | AttackPlayer
