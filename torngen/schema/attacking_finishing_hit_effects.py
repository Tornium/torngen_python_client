import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .attack_finishing_hit_effect import AttackFinishingHitEffect


@dataclass
class AttackingFinishingHitEffects(BaseSchema):
    """
    JSON object of `AttackingFinishingHitEffects`.
    """

    value: int
    name: AttackFinishingHitEffect

    @staticmethod
    def parse(data):
        return AttackingFinishingHitEffects(
            value=BaseSchema.parse(data.get("value"), int),
            name=BaseSchema.parse(data.get("name"), AttackFinishingHitEffect),
        )
