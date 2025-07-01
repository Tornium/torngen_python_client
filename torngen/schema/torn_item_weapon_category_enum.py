from ..base_schema import BaseSchema


class TornItemWeaponCategoryEnum(BaseSchema):

    values = [
        "Melee",
        "Secondary",
        "Primary",
        "Temporary",
    ]
