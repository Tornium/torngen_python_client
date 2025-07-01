from ..base_schema import BaseSchema


class AttackActionEnum(BaseSchema):

    values = [
        "attackerhosp",
        "busy",
        "critical hit",
        "attackerjail",
        "escapefail",
        "hit",
        "hosp",
        "joinfight",
        "leave",
        "loot",
        "lost",
        "missed",
        "mug",
        "noAmmo",
        "onItemUseEff",
        "opponenthosp",
        "opponentjail",
        "paralyzed",
        "reload",
        "runaway",
        "specialTemp",
        "specialTempI",
        "stalemate",
        "startfight",
        "stunned",
        "suppressed",
        "timeout",
        "won",
    ]
