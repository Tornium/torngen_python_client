import typing

from AttackFinishingHitEffect import AttackFinishingHitEffect

from ..base_schema import BaseSchema


class AttackingFinishingHitEffects(BaseSchema):

    value: int
    name: AttackFinishingHitEffect
