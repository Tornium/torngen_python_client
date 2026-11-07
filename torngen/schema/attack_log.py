import typing
from dataclasses import dataclass

from ..base_schema import BaseSchema
from .attack_action_enum import AttackActionEnum
from .attack_log_attacker import AttackLogAttacker
from .attack_log_defender import AttackLogDefender
from .attack_log_item import AttackLogItem


@dataclass
class AttackLog(BaseSchema):
    """
    JSON object of `AttackLog`.
    """

    timestamp: int
    text: str
    icon: str
    defender: None | AttackLogDefender
    attacker_item: typing.Optional[None | AttackLogItem]
    attacker: None | AttackLogAttacker
    action: AttackActionEnum

    @staticmethod
    def parse(data):
        return AttackLog(
            timestamp=BaseSchema.parse(data.get("timestamp"), int),
            text=BaseSchema.parse(data.get("text"), str),
            icon=BaseSchema.parse(data.get("icon"), str),
            defender=BaseSchema.parse(data.get("defender"), None | AttackLogDefender),
            attacker_item=BaseSchema.parse(
                data.get("attacker_item"), typing.Optional[None | AttackLogItem]
            ),
            attacker=BaseSchema.parse(data.get("attacker"), None | AttackLogAttacker),
            action=BaseSchema.parse(data.get("action"), AttackActionEnum),
        )
