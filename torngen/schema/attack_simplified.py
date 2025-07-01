import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .attack_code import AttackCode
from .attack_id import AttackId
from .attack_player_simplified import AttackPlayerSimplified
from .faction_attack_result import FactionAttackResult


@dataclass
class AttackSimplified(BaseSchema):
    """
    JSON object of `AttackSimplified`.
    """

    started: int
    result: FactionAttackResult
    respect_loss: int | float
    respect_gain: int | float
    id: AttackId
    ended: int
    defender: AttackPlayerSimplified
    code: AttackCode
    attacker: None | AttackPlayerSimplified

    @staticmethod
    def parse(data):
        return AttackSimplified(
            started=BaseSchema.parse(data.get("started"), int),
            result=BaseSchema.parse(data.get("result"), FactionAttackResult),
            respect_loss=BaseSchema.parse(data.get("respect_loss"), int | float),
            respect_gain=BaseSchema.parse(data.get("respect_gain"), int | float),
            id=BaseSchema.parse(data.get("id"), AttackId),
            ended=BaseSchema.parse(data.get("ended"), int),
            defender=BaseSchema.parse(data.get("defender"), AttackPlayerSimplified),
            code=BaseSchema.parse(data.get("code"), AttackCode),
            attacker=BaseSchema.parse(
                data.get("attacker"), None | AttackPlayerSimplified
            ),
        )
