from ..base_schema import BaseSchema


class TornItemAmmoTypeEnum(BaseSchema):

    values = [
        "Standard",
        "Hollow Point",
        "Piercing",
        "Tracer",
        "Incendiary",
    ]
