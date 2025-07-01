import typing

from FactionPositionAbilityEnum import FactionPositionAbilityEnum

from ..base_schema import BaseSchema


class FactionPosition(BaseSchema):

    name: str
    is_default: bool
    abilities: typing.List[FactionPositionAbilityEnum]
