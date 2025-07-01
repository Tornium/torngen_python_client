import typing

from AttackCode import AttackCode
from AttackId import AttackId
from AttackPlayerSimplified import AttackPlayerSimplified
from FactionAttackResult import FactionAttackResult

from ..base_schema import BaseSchema


class AttackSimplified(BaseSchema):

    started: int
    result: FactionAttackResult
    respect_loss: int | float
    respect_gain: int | float
    id: AttackId
    ended: int
    defender: AttackPlayerSimplified
    code: AttackCode
    attacker: None | AttackPlayerSimplified
