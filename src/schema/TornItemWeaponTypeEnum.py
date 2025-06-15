from ..base_schema import BaseSchema


class TornItemWeaponTypeEnum(BaseSchema):

    values = [
        "Heavy artillery",
        "Machine gun",
        "Pistol",
        "Rifle",
        "Shotgun",
        "SMG",
        "Temporary",
        "Clubbing",
        "Piercing",
        "Slashing",
        "Mechanical",
    ]
