import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .attack_code import AttackCode
from .attack_id import AttackId
from .attack_player import AttackPlayer
from .attacking_finishing_hit_effects import AttackingFinishingHitEffects
from .faction_attack_result import FactionAttackResult


@dataclass
class Attack(BaseSchema):
    """
    JSON object of `Attack`.
    """

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

    @staticmethod
    def parse(data):
        return Attack(
            started=BaseSchema.parse(data.get("started"), int),
            result=BaseSchema.parse(data.get("result"), FactionAttackResult),
            respect_loss=BaseSchema.parse(data.get("respect_loss"), int | float),
            respect_gain=BaseSchema.parse(data.get("respect_gain"), int | float),
            modifiers=BaseSchema.parse(
                data.get("modifiers"),
                typing.TypedDict(
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
                ),
            ),
            is_stealthed=BaseSchema.parse(data.get("is_stealthed"), bool),
            is_ranked_war=BaseSchema.parse(data.get("is_ranked_war"), bool),
            is_raid=BaseSchema.parse(data.get("is_raid"), bool),
            is_interrupted=BaseSchema.parse(data.get("is_interrupted"), bool),
            id=BaseSchema.parse(data.get("id"), AttackId),
            finishing_hit_effects=BaseSchema.parse(
                data.get("finishing_hit_effects"),
                typing.List[AttackingFinishingHitEffects],
            ),
            ended=BaseSchema.parse(data.get("ended"), int),
            defender=BaseSchema.parse(data.get("defender"), AttackPlayer),
            code=BaseSchema.parse(data.get("code"), AttackCode),
            chain=BaseSchema.parse(data.get("chain"), int),
            attacker=BaseSchema.parse(data.get("attacker"), None | AttackPlayer),
        )
